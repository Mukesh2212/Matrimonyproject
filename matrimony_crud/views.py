from django.shortcuts import render
from matrimony_crud.models import *
from matrimony_crud.serializers import *
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.exceptions import NotFound
from matrimony_crud.models import UserCompatibilityMatch
from datetime import datetime, timedelta
from django.utils import timezone


class HolaApi(APIView):
    def post(self,request,format=None):
        serializer = HolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk=None,format=None):
        id = pk 
        if id is not None:
            hola = HolaModel.objects.get(id=id)
            serializer = HolaSerializer(hola)
            return Response(serializer.data)
        hola = HolaModel.objects.all()
        serializer = HolaSerializer(hola, many = True) 
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        id = pk
        hola = HolaModel.objects.get(id=pk)
        serializer = HolaSerializer(hola,data=request.data)
        if serializer.is_valid():
            return Response({'msg':'data updated','updated-data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk, format=None):
        id = pk 
        hola = HolaModel.objects.get(pk=id)
        hola.delete()
        return Response({'msg':'data has been deleted '})
    

class SixImageApi(APIView):
    def post(self,request,format=None):
        serializer = SixImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Images':'Images has created now ','six_images':serializer.data,'status':status.HTTP_201_CREATED})
        return Response(serializer.errors)
    
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            img = HolaSixPhoto.objects.get(id=id)
            serializer = SixImageSerializer(img)
            return Response(serializer.data)
        img = HolaSixPhoto.objects.all()
        serializer = SixImageSerializer(img, many=True)
        return Response({'All Images':serializer.data})
    
    def put(self,request,pk, format=None):
        id = pk 
        siximg = HolaSixPhoto.objects.get(id=pk)
        serializer = SixImageSerializer(siximg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data has updated successfully','updated_data':serializer.data})
        return Response(serializer.errors) 
    
    def delete(self,request,pk, format=None):
        id = pk 
        siximg = HolaSixPhoto.objects.get(pk=id)
        siximg.delete()
        return Response({'Msg':'data has deleted successfully'})
    

class IdProofApiview(APIView):
    def post(self,request,format=None):
        serializer = IdProofSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':serializer.data,'status':status.HTTP_201_CREATED})
        
    def get(self,request,pk=None, format=None):
        id = pk 
        if id is not None:
            idproof = IdProof.objects.get(id=id)
            serializer = IdProofSerializer(idproof) 
            return Response(serializer.data) 
        idproof = IdProof.objects.all()
        serializer = IdProofSerializer(idproof , many = True) 
        return Response({'Msg':serializer.data})
    
    def put(self,request,pk, format=None):
        id = pk 
        idproof = IdProof.objects.get(id=pk)
        serializer = IdProofSerializer(idproof,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'data has updated successfully','updated_data':serializer.data})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id = pk 
        idproof = IdProof.objects.get(pk=id)
        idproof.delete()
        return Response({'Msg':'data has deleted successfully'})
    

class DocumentApiview(APIView):
    def post(self,request,format=None):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data has created successfully','created_data':serializer.data})
        return Response(serializer.errors) 
    
    def get(self,request,pk=None,format=None):
        id = pk 
        if id is not None:
            document = DocumentAddress.objects.get(id=id)
            serializer = DocumentSerializer(document)
            return Response({'All data':serializer.data})
        document = DocumentAddress.objects.all()
        serializer = DocumentSerializer(document, many=True) 
        return Response({'All data':serializer.data})
    
    def put(self,request,pk,format=None):
        id = pk 
        document = DocumentAddress.objects.get(id=pk)
        serializer = DocumentSerializer(document,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':'Data has updated successfully','Updated_data':serializer.data})
        return Response(serializer.errors)


    def delete(self,request,pk,format=None):
        id = pk 
        document = DocumentAddress.objects.get(pk=id)
        document.delete()
        return Response({'Msg':'Data has deleted successfully'})


class CompatibilityApiview(APIView):
    def post(self,request, format=None):
        serializer = CompatibilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Created data":serializer.data})
        return Response(serializer.errors)
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            compatibilits = CompatibilityMatch.objects.get(id=id)
            serializer = CompatibilitySerializer(compatibilits)    
            return Response({"All_data":serializer.data})   
        compatibility = CompatibilityMatch.objects.all()
        serializer = CompatibilitySerializer(compatibility,many=True) 
        return Response({"All_data":serializer.data}) 
    
    def put(self,request,pk,format=None):
        id = pk 
        compatibility = CompatibilityMatch.objects.get(id=id)
        serializer = CompatibilitySerializer(compatibility,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg":"Data has updated successfully",'Updated_data':serializer.data})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id = pk 
        compatibility = CompatibilityMatch.objects.get(pk=id)
        compatibility.delete()
        return Response({'Msg':'Data has deleted successfully'})
    

class ReviewsApi(APIView):              
    def post(self,request,format=None,*args, **kwargs):  
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg':serializer.data,'status':status.HTTP_201_CREATED})
        return Response(serializer.errors)
        
    def get(self, request, pk=None,format=None):
        id = pk 
        if id is not None:
            review = ReviewSection.objects.get(id=id)
            serializer = ReviewSerializer(review)
            return Response(serializer.data) 
        review = ReviewSection.objects.all()
        serializer = ReviewSerializer(review,many=True) 
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        id = pk 
        review = ReviewSection.objects.get(pk=id)
        serializer = ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Updated_data':serializer.data,'Msg':'Data updated successfully'})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        id = pk 
        review = ReviewSection.objects.get(pk=id)
        review.delete()
        return Response({'Msg':'Data has deleted successfully '})
    

class ProfileCompletationsApiview(APIView):
    def get(self,request,pk=None,  format=None):
        id = pk 
        user_profile = ProfileCompletes.objects.get(pk=id)
        completion_percentage = 0
        
        if user_profile.profile_photo:
            completion_percentage += 10
        if user_profile.basic_details_completed:
            completion_percentage += 15
        if user_profile.education_details_completed:
            completion_percentage += 15
        if user_profile.horoscope_details_completed:
            completion_percentage += 15
        if user_profile.family_details_completed:
            completion_percentage += 15
        if user_profile.partner_preference_details_completed:
            completion_percentage += 15
        if user_profile.habits_details_completed:
            completion_percentage += 5
        if user_profile.hobbies_details_completed:
            completion_percentage += 5
        if user_profile.interest_details_completed:
            completion_percentage += 5
        return Response({'completion_percentage': completion_percentage})

class CompatibilityMatchuser(APIView):
    def get(self,request,pk=None,format=None):
        id = pk 
        if id is not None:
            try:
                user_compatibility = UserCompatibilityMatch.objects.get(id=id)
                # user_profile = UserProfileMutual.objects.first()
            except UserCompatibilityMatch.DoesNotExist:
                raise NotFound("User profile not found")   
            
            user_compatibility_match = UserCompatibilityMatch.objects.filter(
                How_often_do_you_go_out = user_compatibility.How_often_do_you_go_out,
                How_would_you_describe_your_clothes = user_compatibility.How_would_you_describe_your_clothes,
                How_do_you_spend_your_free_time = user_compatibility.How_do_you_spend_your_free_time,
                How_many_times_do_you_visit_salon_or_beauty_parlour = user_compatibility.How_many_times_do_you_visit_salon_or_beauty_parlour,
                How_many_times_do_you_go_out_drinking_or_in_a_pub = user_compatibility.How_many_times_do_you_go_out_drinking_or_in_a_pub,
                What_would_you_choose_for_a_romantic_date_with_your_partner = user_compatibility.What_would_you_choose_for_a_romantic_date_with_your_partner,
                Which_social_platform_do_you_use_Most = user_compatibility.Which_social_platform_do_you_use_Most,
                Do_you_like_shopping = user_compatibility.Do_you_like_shopping,
                Preferences_while_traveling = user_compatibility.Preferences_while_traveling,
                Which_personality_are_you = user_compatibility.Which_personality_are_you
            )
            serializer = UserCompatibilityMatchSerializer(user_compatibility_match,many=True) 
            return Response({'Compatibility_matched_user':serializer.data})
        today = timezone.now().date()
        last_3_days = today - timedelta(days=3)
        last_7_days = today - timedelta(days=7)
        last_30_days = today - timedelta(days=30)
        filter_param = request.GET.get('filter')
        if filter_param == 'today':
            user_profile = UserCompatibilityMatch.objects.filter(created_at=today)
        elif filter_param == 'last_3_days':
            user_profile = UserCompatibilityMatch.objects.filter(created_at__gte=last_3_days)
        elif filter_param == 'last_7_days':
            user_profile = UserCompatibilityMatch.objects.filter(created_at__gte=last_7_days)
        elif filter_param == 'last_30_days':
            user_profile = UserCompatibilityMatch.objects.filter(created_at__gte=last_30_days)
        else:
            user_profile = UserCompatibilityMatch.objects.all() 
        # serializer = UserProfileSerializer(user_profile,many=True)
        return Response({"User_Preference_Partner":user_profile.values()})
    

