from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
import environs
import requests
import json

from .serializers import OrderSerializer
from .models import Order, OrderSet
from core.logger import l

env = environs.Env()
env.read_env()


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
                l.info(data)
                details = json.loads(
                    data.get("Metadata").get("ExtraAttributes")[0]["Value"]
                )
                l.info(details)
                orders = details.pop("orders")
                orderset_list = []
                for product in orders:
                    l.info(f"The current in process product: {product}")
                    order = OrderSet.objects.create(**product)
                    orderset_list.append(order.id)

                obj = Order(**details)
                obj.sale_status = "💸 Payed"
                obj.save()
                obj.orders.set(orderset_list)
                l.info("RESULT HERE -------------------->")
                return JsonResponse({"message": "Payment status updated"}, status=200)
            return JsonResponse(data={"msg": "Payment in pending!"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
