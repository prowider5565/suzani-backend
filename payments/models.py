from django.db import models

from accounts.models import BaseModel


class Order(BaseModel):
    CHOICES = (
        ("💸 Payed", "💸 Payed"),
        ("✈️ On delivery", "✈️ On delivery"),
        ("🟢 Delivered", "🟢 Delivered"),
    )
    full_name = models.CharField(max_length=255)
    address = models.TextField(max_length=10000)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    sale_amount = models.FloatField(default=0, null=False)
    phone_number = models.CharField(max_length=100)
    payment_url = models.URLField(max_length=400, default="https://www.google.com")
    orders = models.ManyToManyField(to="products.Product")
    sale_status = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self) -> str:
        return f"Order for user: {self.full_name} Status: {self.sale_status}"

class OrderSet(BaseModel):
    product = models.ForeignKey(to="products.Product")
    count = models.PositiveSmallIntegerField()

{
    "Source": "Card",
    "IdempotencyKey": None,
    "PaymentId": "F276D59679204FFD84C0F5695",
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
    "CreateDate": 638622772129734224,
    "CreateDateIso": "2024-09-18T17:26:52.9734224Z",
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
