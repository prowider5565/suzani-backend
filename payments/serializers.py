from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "full_name",
            "address",
            "sale_amount",
            "country",
            "phone_number",
            "region",
            "orders",
        ]


{
    "Source": "Card",
    "IdempotencyKey": None,
    "PaymentId": "3F437B330D9247C98E3D390CF",
    "Type": "JustPay",
    "Sandbox": True,
    "PaymentStatus": "Draft",
    "Amount": 500.0,
    "FinalAmount": None,
    "Currency": "USD",
    "RRN": None,
    "Commission": None,
    "Preauthorized": False,
    "CanBeCaptured": False,
    "CreateDate": 638622744222986845,
    "CreateDateIso": "2024-09-18T16:40:22.2986845Z",
    "CaptureDate": None,
    "CaptureDateIso": None,
    "BlockDate": None,
    "BlockDateIso": None,
    "Token": None,
    "CardMask": None,
    "CardOrigination": None,
    "CardOwnerEntityType": None,
    "CardBrand": None,
    "CardCountry": None,
    "CardHolder": None,
    "ExpirationDate": None,
    "SecureCardId": None,
    "RejectionReason": None,
    "Refund": {
        "RefundId": None,
        "Status": None,
        "Refundable": False,
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
        "ExtraAttributes": [
            {
                "Key": "full_name",
                "Value": "Abdusamad ABdullaxanov",
                "Description": "desc1",
            },
            {"Key": "address", "Value": "Earth", "Description": "desc1"},
            {"Key": "sale_amount", "Value": "500", "Description": "desc1"},
            {"Key": "country", "Value": "Uzbekistan", "Description": "desc1"},
            {"Key": "phone_number", "Value": "+998940000000", "Description": "desc1"},
            {"Key": "region", "Value": "Tashkent", "Description": "desc1"},
        ],
    },
    "Payer": {"Phone": None, "FullName": None},
}
