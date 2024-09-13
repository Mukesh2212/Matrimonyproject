from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status , viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from profileapi.models import *
from basicinformationpage.models import *
from educationdetails.models import * 
from familydetails.models import * 
from horoscopedetails.models import * 
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import NotFound



# class Profile_register(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

# class Profile_registerView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

class ProfileRegister(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def get(self, request, *args, **kwargs):
        Family = Profile.objects.all()
        serializer = ProfileSerializer(Family, many=True)
        return Response(serializer.data)

    def post(self, request,*args,**kwargs):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Profile_registerUpdateDeleteView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Profile, pk=pk)

    def get(self, request, pk):
        search = self.get_object(pk)
        serializer = ProfileSerializer(search)
        return Response(serializer.data)

    def put(self, request, pk):
        search = self.get_object(pk)
        serializer = ProfileSerializer(search, data=request.data, partial=True)

        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        search = self.get_object(pk)
        search.delete()
        return Response({"message":"Delete Successfully!!!"},status=status.HTTP_204_NO_CONTENT)
    



class ProfileCompletionsAPIView(APIView):
    def get(self, request , pk=None,format=None):
        id = pk 
        if id is not None:
            profile_ojb = ProfileCompletionsApi.objects.get(id=id)
            serializer = ProfileCompletionsSerializer(profile_ojb)
            return Response(serializer.data)
        profiles = ProfileCompletionsApi.objects.all()
        serializer = ProfileCompletionsSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileCompletionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            data = serializer.validated_data
            basic_information = 15 if data.get('basic_information') else 0
            profile_photo = 10 if data.get('profile_photo') else 0
            education_details = 15 if data.get('education_details') else 0
            horoscope_details = 15 if data.get('horoscope_details') else 0
            partner_prefrence = 15 if data.get('partner_prefrence') else 0
            family_details = 15 if data.get('family_details') else 0
            habits = 5 if data.get('habits') else 0
            hobbies = 5 if data.get('hobbies') else 0
            interest = 5 if data.get('interest') else 0

            total_score = (basic_information + profile_photo + education_details +
                           horoscope_details + partner_prefrence + family_details +
                           habits + hobbies + interest)
            
            
            return Response({
                # 'serializer_data': serializer.data,
                'basic_information': basic_information,
                'profile_photo': profile_photo,
                'education_details': education_details,
                'horoscope_details': horoscope_details,
                'partner_prefrence': partner_prefrence,
                'family_details': family_details,
                'habits': habits,
                'hobbies': hobbies,
                'interest': interest,
                'profile_completion_score': total_score
            })
            
            
        return Response(serializer.errors, status=400)
    

class MutualProfileMatching(APIView):
    def get(self, request, pk,format=None):
        id = pk 
        if id is not None:
            user_profile = Profile.objects.get(id=id)
            current_user_gender = user_profile.gender
            current_user_age = user_profile.age
            curerent_user_image = user_profile.image
            current_user_name = user_profile.name
            current_user_email = user_profile.email
            current_user_PhoneNumber = user_profile.PhoneNumber
            current_user_address = user_profile.address
            current_user_state = user_profile.state 
            current_user_city = user_profile.city
            current_user_zipcode = user_profile.zipcode
            current_user_date = user_profile.date
            current_user_religion = user_profile.religion
            currrent_user_caste = user_profile.caste
            current_user_height = user_profile.height
            current_user_education = user_profile.education
            current_user_occupation = user_profile.occupation
            current_user_income = user_profile.income


            mutual_profiles = Profile.objects.filter(gender=current_user_gender, age=current_user_age,image=curerent_user_image,
                                                     name=current_user_name,email=current_user_email,PhoneNumber=current_user_PhoneNumber,
                                                     address=current_user_address,state=current_user_state,city=current_user_city,
                                                     zipcode=current_user_zipcode,date=current_user_date,religion=current_user_religion,
                                                     caste=currrent_user_caste,height=current_user_height,education=current_user_education,
                                                     occupation=current_user_occupation,income=current_user_income)
            serializer = ProfileSerializer(mutual_profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        user_profile = Profile.objects.all()
        serializer = ProfileSerializer(user_profile,many=True) 
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new profile
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        try:
            mutual_profile = Profile.objects.get(id = pk)
        except Profile.DoesNotExist:    
            return Response({'error': 'Mutual profile not found'}, status=status.HTTP_404_NOT_FOUND)    
        serializer = ProfileSerializer(mutual_profile,data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Updated Data':serializer.data}) 
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        try:
            mutual_profile = Profile.objects.get(id=pk)
        except Profile.DoesNotExist:
            return Response({'error': 'Mutual profile not found'}, status=status.HTTP_404_NOT_FOUND)

        mutual_profile.delete()
        return Response({'message': 'Mutual profile deleted successfully'}, status=status.HTTP_204_NO_CONTENT)