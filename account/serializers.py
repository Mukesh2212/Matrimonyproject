from rest_framework import serializers
from account.models import *
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util 
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
# from django.contrib.auth import get_user_model
from django.conf import settings

# User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  # password = serializers.CharField(style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

  class Meta:
    model = User
    fields=['email', 'name', 'password','phoneNumber', 'password2', 'tc']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    # email = attrs.get('email')
    # phoneNumber = attrs.get('phoneNumber')
    # otp = attrs.get('otp')
    # if not email:
    #   raise serializers.ValidationError("please enter valid email ")
    
    # if not phoneNumber:
    #   raise serializers.ValidationError("please enter valid phone number ")
    
    # if not otp:
    #   raise serializers.ValidationError("please enter valid otp ")
    
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)

class OTPVerificationSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    otp = serializers.CharField(required=False)

    def validate(self,attrs):
      otp = attrs.get('otp')
      email = attrs.get('email')
      phoneNumber = attrs.get('phoneNumber')

      try:
            otp_instance = User.objects.get(email=email, phoneNumber=phoneNumber,otp=otp)
      except User.DoesNotExist:
            raise serializers.ValidationError("Invalid country code or phone number or invalid otp , please check once again")
      return attrs
  

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']



class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'name',] 


class UserChangePasswordSerializer(serializers.Serializer):
  password  =  serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 =  serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    user = self.context.get('user')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    user.set_password(password)
    user.save()
    return attrs

import requests

# url = "https://hourmailer.p.rapidapi.com/send"
url = "https://mail-sender-api1.p.rapidapi.com/"
# url =  "https://demo-project67614.p.rapidapi.com/catalog/product"


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = f'https://madmin.hola9.com/api/user/reset-password/{uid}/{token}/'
            print('Password Reset Link', link)

            # Prepare the email content
            subject = 'Reset Your Password'
            message = f'Click on the following link to reset your password: {link}'
            recipient_list = [email]
            from_email = settings.DEFAULT_FROM_EMAIL  # Ensure this is set in your settings.py
            
            # Send email using Django's send_mail method
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            print('Password reset email sent successfully.')
            return attrs
        else:
            raise serializers.ValidationError('You are not a registered user')

    

class UserPasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      password2 = attrs.get('password2')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      id = smart_str(urlsafe_base64_decode(uid))
      user = User.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      user.set_password(password)
      user.save()
      return attrs
    except DjangoUnicodeDecodeError as identifier:
      PasswordResetTokenGenerator().check_token(user, token)
      raise serializers.ValidationError('Token is not Valid or Expired')    