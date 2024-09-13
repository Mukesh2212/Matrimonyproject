from django.shortcuts import render
import os
import random
import math
# *********************** FOR OTP SEND TO MOBILE NUMBER **********************************
#******************* START  *****************************

# ***************** END SEND OTP ***************************

# * Rest Framework Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view

# * Twilio Imports
# from twilio.rest import Client


# * models Import
from .models import OTPVerifiaction,PhoneUser
# from .models import CustomUser

#* Errors
# from django.db import IntegrityError


# * Generating OTP
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


# *Checks OTP with the otp recevied from the GET Request

def generatingOTP(number):
    OTP = generateOTP()

    return OTP


# * Checking the OTP
import requests

url = "https://www.fast2sms.com/dev/bulkV2"
@api_view(['GET', 'POST'])
def otpGeneration(request):
    number = request.data['number']
    print(number)
    generatedOTP = generatingOTP(number)
    print(generatedOTP)
    s=OTPVerifiaction.objects.filter(phone_number=number).delete()
    print("end")  
    # querystring = {"authorization":"FlksSDzg13vfLoUreKH9xh6CbXIA42OVynQduMPG0Bm7Ja5c8qdaBRD5fUS4lT0EX2HzV9rtAcInkZxK","variables_values":generatedOTP,"route":"otp","numbers":number}
    querystring = {"authorization":"NYUAGPHmCO27kq39ir8WB6txeTuFXhEIsSdcoMp0gfyvJ1aDwLQbBluGHPZeV0iOCjLwfxvsYyoWgTaM","variables_values":generatedOTP,"route":"otp","numbers":number}
    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print("start")
    print(response.text)
    if generatedOTP:
        data = OTPVerifiaction(phone_number=number, otp=generatedOTP)
        data.save()
        print(generatedOTP)
        return Response({"OTPSent": True})
    else:
        return Response({"OTPSent": False})


@api_view(['PUT'])
def checkOTP(request):
    number = request.data['number']
    otp = request.data['otp']
    print("checking time",number,otp)
    generatedOTP = OTPVerifiaction.objects.filter(
        phone_number=number).values_list('otp')
    print(generatedOTP)
    if generatedOTP[0][0] == otp:
        data = OTPVerifiaction.objects.get(phone_number=number)
        data.is_verfied = True
        data.save()
        return Response({"status": True})

    else:
        return Response({"status": False})


# @api_view(['POST'])
# def registerUser(request):
#     contact_number = request.data['number']
#     password = request.data['password']
#     user = CustomUser(user_name = user_name)
#     user.email = email
#     user.contact_number = contact_number
#     user.set_password(password)
#     try:
#         user.save()
#         otp_clutter = OTPVerifiaction.objects.get(phone_number = contact_number)
#         otp_clutter.delete()
#         return Response({"IntegrityError": False})
#     except IntegrityError as e:
#         return Response({"IntegrityError" : True})
    



@api_view(['GET', 'POST'])
def verifyUserPhone(request):
    phoneNumber=request.data['number']
    s=PhoneUser.objects.filter(phone_number=phoneNumber)
    print(s)
    if s:
        return Response({"status": "exist user"})
    else:
        return Response({"status":"not Exist"})

@api_view(['GET', 'POST'])
def sendMessage(request):
    sender=request.data['sender']
    title=request.data['title']
    message=request.data['message']
    phoneNumber=request.data['phoneNumber']
    textValue="Hola9-"+title+"-"+phoneNumber +" -"+message
    print(textValue)
    querystring = {"authorization":"FlksSDzg13vfLoUreKH9xh6CbXIA42OVynQduMPG0Bm7Ja5c8qdaBRD5fUS4lT0EX2HzV9rtAcInkZxK","variables_values":textValue,"route":"otp","numbers":sender}
    # querystring = {"authorization":"NYUAGPHmCO27kq39ir8WB6txeTuFXhEIsSdcoMp0gfyvJ1aDwLQbBluGHPZeV0iOCjLwfxvsYyoWgTaM","variables_values":textValue,"route":"otp","numbers":sender}
    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return Response({"status": "success"})



from rest_framework.views import APIView
from rest_framework.response import Response
from twilio.rest import Client
from otp_reg.models import *
from django.conf import settings 
from otp_reg.serializers import *
from datetime import datetime, timedelta
from rest_framework import status 
from account.models import User 
from rest_framework_simplejwt.tokens import RefreshToken
from account.serializers import * 
from django.core.mail import send_mail


class MobileNumberFetch(APIView):
    def get(self, request, pk, format=None):
        try:
            user = User.objects.get(id=pk)
            user_mobile = user.phoneNumber  
            otp = random.randint(100000, 999999)
            return Response({'User_mobile_otp': user_mobile , 'user_otp': otp})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
        
class EmailFetch(APIView):
    def get(self,request,pk,format=None):
        try:
            user = User.objects.get(id=pk)
            user_email = user.email 
            otp = random.randint(100000,999999) 
            subject = 'Your OTP for getting email of matrimony project'
            message = f'Your OTP is: {otp}'
            from_email = 'mk2648054@gmail.com' 
            recipient_list = ['mk2648054@gmail.com']
            send_mail(subject, message, from_email, recipient_list)
            return Response({'user_email':user_email,'User_email':'Otp has sent on your register email'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)   