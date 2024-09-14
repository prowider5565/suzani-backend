from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
import environs
import requests
import json

from .serializers import OrderSerializer
from core.logger import l

env = environs.Env()
env.read_env()


@api_view(["POST"])
def start_payment_process(request):
    customer_serializer = OrderSerializer(data=request.data)
    customer_serializer.is_valid(raise_exception=True)
    payload = {
        "source": "Card",
        "amount": customer_serializer.validated_data["sale_amount"],
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
                {"key": "key1", "value": "val2", "description": "desc1"}
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
        customer_serializer.validated_data["payment_url"] = payment_url
        customer_serializer.validated_data["sale_status"] = "💸 Payed"
        customer_serializer.save()
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
            payment_id = data.get("payment_id")
            status = data.get("status")
            return JsonResponse({"message": "Payment status updated"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
