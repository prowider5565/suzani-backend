from paycomuz.views import MerchantAPIView

from .validators import CheckOrder


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder
