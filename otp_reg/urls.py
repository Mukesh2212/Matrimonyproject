from django.urls import path
from otp_reg.views import *
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)


urlpatterns = [
    path('checkOTP/', checkOTP ),
    path('sendOTP/',otpGeneration),
    path('verifyUserPhone/',verifyUserPhone),
    path('sendMessage/',sendMessage),
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('usermobile/<int:pk>/', MobileNumberFetch.as_view()),
    path('useremail/<int:pk>/', EmailFetch.as_view()),
]