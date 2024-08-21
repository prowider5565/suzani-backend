from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from django_redis import get_redis_connection
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.db import IntegrityError
from drf_yasg import openapi
import json

from .serializers import UserAccountSerializer, OTPSerializer


@swagger_auto_schema(
    method="post",
    request_body=UserAccountSerializer,
    responses={
        200: openapi.Response(
            description="Email verification initiated",
            examples={"application/json": {"msg": "random_key"}},
        ),
        400: openapi.Response(
            description="Bad request",
            examples={"application/json": {"msg": "Email is required"}},
        ),
    },
)
@api_view(["POST"])
def send_email_verification(request):
    serializer = UserAccountSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    incoming_email = serializer.validated_data["email"]
    if get_user_model().objects.filter(email=incoming_email).exists():
        return Response(
            {"msg": f"User with email: {incoming_email} already exists!"}, status=400
        )
    # Get a connection to Redis
    connection = get_redis_connection()
    # randint = generate_random_digit()
    randint = "111111"
    data = json.dumps(serializer.validated_data)
    connection.set(randint, data)

    # Send a notification to the given email
    subject = "Verification email for Ecommerce Suzane"
    body = f"""
    Your email is verified successfully! 
    To continue your registration, you will need this OTP code: {randint}
    """
    email = EmailMessage(subject=subject, body=body, to=[incoming_email])
    email.send()

    return Response(
        {
            "msg": f"Verification sent to email: {serializer.validated_data['email']}, {randint}"
        },
        status=200,
    )


class RegistrationAPIView(CreateAPIView):
    serializer_class = OTPSerializer
    model = get_user_model()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Get random digit from redis by filtering by uuid
        connection = get_redis_connection()
        data = connection.get(serializer.validated_data["otp"])
        if data is None:
            return Response({"msg": f"Invalid or expired OTP code!"}, status=401)
        user_credentials = json.loads(data)
        # Delete the OTP code from redis after successful registration
        connection.delete(serializer.validated_data["otp"])
        try:
            if user_credentials["role"] == "manager":
                user_credentials["is_active"] = False
                user = self.model.objects.create_superuser(**user_credentials)
            else:
                user = self.model.objects.create_user(**user_credentials)
        except IntegrityError:
            return Response(
                {
                    "msg": f"User with email: {user_credentials['email']} already exists!"
                },
                status=400,
            )
        refresh = RefreshToken.for_user(user)
        token = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(token)


class UserDetailsAPIView(GenericAPIView):
    serializer_class = UserAccountSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
