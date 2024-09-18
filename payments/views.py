from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
import environs
import requests
import json

from .serializers import OrderSerializer
from core.logger import l
from .models import Order

env = environs.Env()
env.read_env()


@api_view(["POST"])
def start_payment_process(request):
    customer_serializer = OrderSerializer(data=request.data)
    customer_serializer.is_valid(raise_exception=True)
    l.info(customer_serializer.data)
    customer_data = customer_serializer.data
    sale_amount = customer_data["sale_amount"]
    customer_data["orders"] = [str(order_id) for order_id in customer_data["orders"]]
    # customer_data["orders"] = [
    #     {"id": str(order_id), "count": count}
    #     for order_id, count in customer_data["orders"]
    # ]
    adata = json.dumps(customer_data)
    payload = {
        "source": "Card",
        "amount": sale_amount,
        "currency": "USD",
        "language": "EN",
        "hooks": {
            # env.str("DOMAIN") + "
            "webhookGateway": "https://18e1-84-54-73-7.ngrok-free.app/payments/webhook/",
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
            details = json.loads(
                data.get("Metadata").get("ExtraAttributes")[0]["Value"]
            )
            l.info(details)
            orders = details.pop("orders")
            obj = Order(**details)
            obj.sale_status = "💸 Payed"
            obj.save()
            obj.orders.set(orders)
            l.info("RESULT HERE -------------------->")
            return JsonResponse({"message": "Payment status updated"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
