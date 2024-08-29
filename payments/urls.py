from django.urls import path
from . import views

urlpatterns = [
    path("webhook/", views.payze_webhook, name="payze_webhook"),
    path("process/", views.start_payment_process, name="start_payment_process"),
]
