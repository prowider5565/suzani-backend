from drf_yasg.generators import OpenAPISchemaGenerator
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework import permissions


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(),
)

urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("social/", include("social.urls")),
    path("products/", include("products.urls")),
    path("payments/", include("payments.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

{
    "Source": "Card",
    "IdempotencyKey": None,
    "PaymentId": "64DD2AEC35B548A1AA245D234",
    "Type": "JustPay",
    "Sandbox": True,
    "PaymentStatus": "Captured",
    "Amount": 100.0,
    "FinalAmount": 100.0,
    "Currency": "USD",
    "RRN": None,
    "Commission": None,
    "Preauthorized": False,
    "CanBeCaptured": False,
    "CreateDate": 638604615515552280,
    "CreateDateIso": "2024-08-28T17:05:51.555228Z",
    "CaptureDate": 638604615861461838,
    "CaptureDateIso": "2024-08-28T17:06:26.1461838Z",
    "BlockDate": None,
    "BlockDateIso": None,
    "Token": None,
    "CardMask": "986000xxxxxx0000",
    "CardOrigination": None,
    "CardOwnerEntityType": "Unknown",
    "CardBrand": "Humo",
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
        "ExtraAttributes": [
            {"Key": "key", "Value": "val", "Description": "desc"},
            {"Key": "key1", "Value": "val2", "Description": "desc1"},
        ],
    },
    "Payer": {"Phone": None, "FullName": None},
}
