from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Genearte Token  Manually

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    # token = get_tokens_for_user(user)
    return Response({ 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
  
class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
   
           




class ProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = ProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
  

    
class ChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
    

class ResetPasswordEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Rest Link Send,Please check Your Email.'} , status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ResetPasswordView(APIView):
    def post(self,request,uid,token,format=None):
        serializer = UserPasswordResetSerializer(data=request.data , context = {'uid':uid , 'token':token})  
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Reset Password Successfully'} , status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    

class verifyEmail(APIView):
    def post(self,request,format=None):
      email=request.data.get("email")
      s=User.objects.filter(email=email)
      if s:
        return HttpResponse("already exist",content_type='application/json')
      else:
        return HttpResponse("not exist",content_type='application/json')     

class verifyPhone(APIView):
    def post(self,request,format=None):
      phoneNumber=request.data.get("phoneNumber")
      print(phoneNumber)
      # s1=User.objects.filter(email=email)
      # s=User.objects.filter(phoneNumber=phoneNumber)
      try:
        user = User.objects.get(phoneNumber=phoneNumber)
        token = get_tokens_for_user(user)
      except:
        user=None
      if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
      else:
        return Response({'errors':{'non_field_errors':['phone Number not exist']}}, status=status.HTTP_404_NOT_FOUND)        

class verifyEmailLogin(APIView):
    def post(self,request,format=None):
      email=request.data.get("email")
      print(email)
      # s1=User.objects.filter(email=email)
      # s=User.objects.filter(phoneNumber=phoneNumber)
      try:
        user = User.objects.get(email=email)
      except:
        user=None
      if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
      else:
        return Response({'errors':{'non_field_errors':['Email not exist']}}, status=status.HTTP_404_NOT_FOUND)       


# import requests
# from django.views.generic.edit import CreateView
# class verify_aadhaar(CreateView):
#   def post(request):
#       aadhaar_number = request.POST.get('aadhaar_number')

#       # Make API call to UIDAI Aadhaar verification API
#       response = requests.post(
#           'https://<UIDAI API endpoint>',
#           data={'aadhaar_number': aadhaar_number},
#           headers={'Authorization': '<UIDAI API access token>'}
#       )

#       if response.status_code == 200:
#           # Aadhaar card is verified
#           return JsonResponse({'status': 'success'})
#       else:
#           # Aadhaar card verification failed
#           return JsonResponse({'status': 'error'})

    

 



        


