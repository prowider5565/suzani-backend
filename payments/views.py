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
    # Retrieve payment valid payload from client
    customer_serializer = OrderSerializer(data=request.data)
    l.info(request)
    customer_serializer.is_valid(raise_exception=True)

    # Payload to send to Service
    payload = {
        "source": "Card",
        "amount": customer_serializer.validated_data["sale_amount"],
        "currency": "USD",
        "language": "EN",
        "hooks": {
            "webhookGateway": "https://042f-83-222-6-203.ngrok-free.app/payments/webhook/",
            "successRedirectGateway": "https://suzani-abdulhakim.uz/",
            "errorRedirectGateway": "https://suzani-abdulhakim.uz/",
        },
        "metadata": {
            "order": {"orderId": "OrderId"},
            "extraAttributes": [
                {"key": "key1", "value": "val2", "description": "desc1"}
            ],
        },
    }

    # Request to Payze Service
    token = f"{env.str('PAYZE_API_KEY')}:{env.str('PAYZE_SECRET_KEY')}"
    headers = {
        "accept": "application/json",
        "content-type": "application/*+json",
        "Authorization": token,
    }
    payment_request = requests.put(
        env.str("PAYZE_REQUEST_URL"), data=json.dumps(payload), headers=headers
    )
    l.info(payment_request.text)
    status = payment_request.status_code
    l.info(f"Status code: {status}")
    response = payment_request.json()
    l.info(response)
    l.info("_____________________________")

    # Collect Payment url, save order to database and return response to client
    payment_url = response.get("data").get("payment").get("paymentUrl")
    if status == 200:
        # Status code is 200, save order to database and return response to client
        l.info(f"Payment URL: {payment_url}")
        l.info("Successful resonse from Payze service")
        customer_serializer.validated_data["payment_url"] = payment_url
        customer_serializer.validated_data["sale_status"] = "pending"
        customer_serializer.save()
        return JsonResponse(
            data={
                "msg": "Ready to process the payment",
                "status": "OK",
                "redirect_url": payment_url,
            }
        )
    else:
        # Failure to process the payment
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
            # Parse the incoming JSON data
            data = json.loads(request.body)
            l.info("Everything coming from Payze Service:")
            l.info("____________________________________")
            l.info(data)
            # Process the data (e.g., update payment status)
            payment_id = data.get("payment_id")
            status = data.get("status")

            # Here, you would update your database or perform other actions
            # Example: update_payment_status(payment_id, status)

            return JsonResponse({"message": "Payment status updated"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)


# def get_payment_redirect_url(request, product_id):
#     # data.payment.paymentUrl
#     # data.payment.createdDate
#     payment_url =
