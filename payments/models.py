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
    payment_url = models.URLField(max_length=400, default="")
    orders = models.ManyToManyField(to="OrderSet")
    sale_status = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self) -> str:
        return f"Order for user: {self.full_name} Status: {self.sale_status}"

    class Meta:
        indexes = [
            models.Index(fields=["sale_amount"]),
        ]


class OrderSet(BaseModel):
    product_name = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(
        to="products.Product", on_delete=models.SET_NULL, null=True
    )
    count = models.PositiveSmallIntegerField()

    def __str__(self):
        product_name = self.product.name if self.product else self.product_name
        return f"📦 {self.count} stick(s) of {product_name}"
