from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('profile/',ProfileView.as_view(), name='profile'),
    
    # change password is working
    path('changepassword/', ChangePasswordView.as_view(), name='changepassword'),
    #is working but not getting mail
    path('send-reset-password-email/', ResetPasswordEmailView.as_view(), name='send-reset-password-email'),
    #reset password uid token is working
    path('reset-password/<uid>/<token>/', ResetPasswordView.as_view(), name='reset-password'),
    # all api is working
    path('verifyEmail/',verifyEmail.as_view(),name='update-verifyEmail'),
    path('verifyPhone/',verifyPhone.as_view(),name='update-verifyPhone'),
    path('verifyEmailLogin/',verifyEmailLogin.as_view(),name='update-verifyEmailLogin'),
    # path('verify-aadhaar/', verify_aadhaar.as_view(), name='verify-aadhaar'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)