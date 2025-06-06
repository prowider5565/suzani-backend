from django.urls import path
from . import views

urlpatterns = [
    path("webhook/", views.payze_webhook, name="payze_webhook"),
    path("process/", views.start_payment_process, name="start_payment_process"),
]

{
    "Source": "Card",
    "IdempotencyKey": None,
    "PaymentId": "4A6B8681FFC14A3089E9051F4",
    "Type": "JustPay",
    "Sandbox": True,
    "PaymentStatus": "Captured",
    "Amount": 500.0,
    "FinalAmount": 500.0,
    "Currency": "USD",
    "RRN": None,
    "Commission": None,
    "Preauthorized": False,
    "CanBeCaptured": False,
    "CreateDate": 638622683990286370,
    "CreateDateIso": "2024-09-18T14:59:59.028637Z",
    "CaptureDate": 638622684213621725,
    "CaptureDateIso": "2024-09-18T15:00:21.3621725Z",
    "BlockDate": None,
    "BlockDateIso": None,
    "Token": None,
    "CardMask": "411111xxxxxx1111",
    "CardOrigination": None,
    "CardOwnerEntityType": "Unknown",
    "CardBrand": "Visa",
    "CardCountry": None,
    "CardHolder": None,
    "ExpirationDate": "1226",
    "SecureCardId": None,
    "RejectionReason": None,
    "Refund": {
        "RefundId": None,
        "Status": None,
        "Refundable": True,
        "Amount": None,
        "RequestedAmount": None,
        "RejectReason": None,
        "RefundDate": None,
        "RefundDateIso": None,
        "Revisions": [],
    },
    "Splits": None,
    "Metadata": {
        "Channel": None,
        "Order": {
            "OrderId": "OrderId",
            "AdvanceContactId": None,
            "OrderItems": [],
            "UzRegulatoryOrderDetails": {
                "Latitude": None,
                "Longitude": None,
                "TaxiVehicleNumber": None,
                "TaxiTin": None,
                "TaxiPinfl": None,
            },
            "BillingAddress": {
                "FirstName": None,
                "LastName": None,
                "City": None,
                "Country": None,
                "Line1": None,
                "Line2": None,
                "PostalCode": None,
                "State": None,
                "PhoneNumber": None,
            },
            "ShippingAddress": {
                "FirstName": None,
                "LastName": None,
                "City": None,
                "Country": None,
                "Line1": None,
                "Line2": None,
                "PostalCode": None,
                "State": None,
                "PhoneNumber": None,
            },
        },
        "ExtraAttributes": [{"Key": "key1", "Value": "val2", "Description": "desc1"}],
    },
    "Payer": {"Phone": None, "FullName": None},
}
