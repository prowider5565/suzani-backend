from django.db import models

from accounts.models import BaseModel


# Create your models here.
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
    sale_status = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self) -> str:
        return f"Order for user: {self.full_name} Status: {self.sale_status}"
