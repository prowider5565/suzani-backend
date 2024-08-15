import paypalrestsdk
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .paypal_config import paypalrestsdk


class CreatePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        payment = paypalrestsdk.Payment(
            {
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "redirect_urls": {
                    "return_url": request.build_absolute_uri("/execute/"),
                    "cancel_url": request.build_absolute_uri("/cancel/"),
                },
                "transactions": [
                    {
                        "item_list": {
                            "items": [
                                {
                                    "name": "item",
                                    "sku": "item",
                                    "price": "5.00",
                                    "currency": "USD",
                                    "quantity": 1,
                                }
                            ]
                        },
                        "amount": {"total": "5.00", "currency": "USD"},
                        "description": "This is the payment transaction description.",
                    }
                ],
            }
        )

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    approval_url = str(link.href)
                    return Response(
                        {"approval_url": approval_url}, status=status.HTTP_201_CREATED
                    )
        else:
            return Response(payment.error, status=status.HTTP_400_BAD_REQUEST)


class ExecutePaymentView(APIView):
    def get(self, request, *args, **kwargs):
        payment_id = request.GET.get("paymentId")
        payer_id = request.GET.get("PayerID")

        payment = paypalrestsdk.Payment.find(payment_id)

        if payment.execute({"payer_id": payer_id}):
            return Response(
                {"status": "Payment executed successfully"}, status=status.HTTP_200_OK
            )
        else:
            return Response(payment.error, status=status.HTTP_400_BAD_REQUEST)
