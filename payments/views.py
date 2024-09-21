from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse
from drf_yasg import openapi
import environs
import requests
import json

from .serializers import OrderSerializer
from .models import Order, OrderSet
from core.logger import l

env = environs.Env()
env.read_env()


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "full_name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Customer's full name",
                example="John Doe",
            ),
            "address": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Customer's address",
                example="1234 Elm St, Apt 5",
            ),
            "country": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Customer's country",
                example="USA",
            ),
            "region": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Customer's region",
                example="California",
            ),
            "sale_amount": openapi.Schema(
                type=openapi.TYPE_NUMBER,
                format=openapi.FORMAT_FLOAT,
                description="Total sale amount",
                example=150.50,
            ),
            "phone_number": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Customer's phone number",
                example="+1 234 567 8900",
            ),
            "orders": openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "order_id": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Order identifier",
                            example="abc123",
                        ),
                        "product_name": openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Product name",
                            example="T-shirt",
                        ),
                        "quantity": openapi.Schema(
                            type=openapi.TYPE_INTEGER,
                            description="Quantity of the product",
                            example=2,
                        ),
                    },
                ),
                description="List of order items",
            ),
        },
        required=["full_name", "sale_amount", "phone_number", "orders"],
    ),
    responses={
        200: openapi.Response(
            description="Payment successfully initiated",
            examples={
                "application/json": {
                    "msg": "Ready to process the payment",
                    "status": "OK",
                    "redirect_url": "https://paymentgateway.com/pay/xyz123",
                }
            },
        ),
        400: openapi.Response(
            description="Invalid input data",
            examples={
                "application/json": {
                    "msg": "Payment Initialization failed!",
                    "error": "Invalid sale_amount",
                    "status": 400,
                }
            },
        ),
        500: openapi.Response(
            description="Server error",
            examples={
                "application/json": {
                    "msg": "Payment Initialization failed!",
                    "error": "Internal server error",
                    "status": 500,
                }
            },
        ),
    },
)
@api_view(["POST"])
def start_payment_process(request):
    customer_serializer = OrderSerializer(data=request.data)
    customer_serializer.is_valid(raise_exception=True)
    adata = customer_serializer.data
    sale_amount = adata["sale_amount"]
    adata = json.dumps(adata)
    payload = {
        "source": "Card",
        "amount": sale_amount,
        "currency": "USD",
        "language": "EN",
        "hooks": {
            "webhookGateway": env.str("DOMAIN") + "/payments/webhook/",
            "successRedirectGateway": env.str("DOMAIN"),
            "errorRedirectGateway": env.str("DOMAIN") + "/failed-payment",
        },
        "metadata": {
            "order": {"orderId": "OrderId"},
            "extraAttributes": [
                {
                    "key": "order_details",
                    "value": adata,
                    "description": "Whole data in json",
                }
            ],
        },
    }
    token = f"{env.str('PAYZE_API_KEY')}:{env.str('PAYZE_SECRET_KEY')}"
    headers = {
        "accept": "application/json",
        "content-type": "application/*+json",
        "Authorization": token,
    }
    payment_request = requests.put(
        env.str("PAYZE_REQUEST_URL"), data=json.dumps(payload), headers=headers
    )
    status = payment_request.status_code
    response = payment_request.json()
    payment_url = response.get("data").get("payment").get("paymentUrl")
    if status == 200:

        return JsonResponse(
            data={
                "msg": "Ready to process the payment",
                "status": "OK",
                "redirect_url": payment_url,
            }
        )
    else:
        return JsonResponse(
            data={
                "msg": "Payment Initialization failed!",
                "error": response,
                "status": status,
            }
        )


@csrf_exempt
def payze_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if data["PaymentStatus"] == "Captured":
                details = json.loads(
                    data.get("Metadata").get("ExtraAttributes")[0]["Value"]
                )
                orders = details.pop("orders")
                orderset_list = []
                for product in orders:
                    order = OrderSet.objects.create(**product)
                    orderset_list.append(order.id)

                obj = Order(**details)
                obj.sale_status = "💸 Payed"
                obj.save()
                obj.orders.set(orderset_list)
                return JsonResponse({"message": "Payment status updated"}, status=200)
            return JsonResponse(data={"msg": "Payment in pending!"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
