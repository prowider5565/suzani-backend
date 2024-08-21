from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.urls import path

from . import views


urlpatterns = [
    path("verify-email/", views.send_email_verification, name="verification"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegistrationAPIView.as_view(), name="registration"),
    path("me/", views.UserDetailsAPIView.as_view()),
]
