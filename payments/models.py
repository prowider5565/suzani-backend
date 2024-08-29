from django.db import models

from accounts.models import BaseModel


# Create your models here.
class Order(BaseModel):
    CHOICES = (
        ("pending", "Pending"),
        ("payed", "Payed"),
        ("on_delivery", "On delivery"),
        ("delivered", "Delivered"),
    )
    full_name = models.CharField(max_length=255)
    address = models.TextField(max_length=10000)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    sale_amount = models.BigIntegerField(default=0)
    phone_number = models.CharField(max_length=100)
    payment_url = models.URLField(max_length=400, default="https://www.google.com")
    sale_status = models.CharField(max_length=50, choices=CHOICES)
