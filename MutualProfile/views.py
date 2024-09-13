from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 
from MutualProfile.models import * 
from MutualProfile.serializers import * 
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter 
from django_filters.rest_framework import DjangoFilterBackend 


class MutualMatchesAPIView(APIView):  
    def get(self, request, pk=None, format=None):
        id = pk 
        if id is not None:
            try:
                user_profile = UserProfileMutual.objects.get(id=id)
                # user_profile = UserProfileMutual.objects.first()
            except UserProfileMutual.DoesNotExist:
                raise NotFound("User profile not found")    
            mutual_profiles = UserProfileMutual.objects.filter(
                looking_for = user_profile.looking_for,
                age_from = user_profile.age_from,
                age_to = user_profile.age_to,
                height_from =user_profile.height_from,
                heigiht_to = user_profile.heigiht_to,
                rellgion = user_profile.rellgion,
                caste = user_profile.caste,
                complexion = user_profile.complexion,
                residency_status = user_profile.residency_status,
                country = user_profile.country,
                education = user_profile.education,
                occupation = user_profile.occupation,
                partner_expectations = user_profile.partner_expectations,
                
            )
            serializer = UserProfileSerializer(mutual_profiles , many=True)        
            return Response({'User_Preference_Partner': serializer.data})
        today = timezone.now().date()
        last_3_days = today - timedelta(days=3)
        last_7_days = today - timedelta(days=7)
        last_30_days = today - timedelta(days=30)
        filter_param = request.GET.get('filter')
        if filter_param == 'today':
            user_profile = UserProfileMutual.objects.filter(created_at=today)
        elif filter_param == 'last_3_days':
            user_profile = UserProfileMutual.objects.filter(created_at__gte=last_3_days)
        elif filter_param == 'last_7_days':
            user_profile = UserProfileMutual.objects.filter(created_at__gte=last_7_days)
        elif filter_param == 'last_30_days':
            user_profile = UserProfileMutual.objects.filter(created_at__gte=last_30_days)
        else:
            user_profile = UserProfileMutual.objects.all() 
        # serializer = UserProfileSerializer(user_profile,many=True)
        return Response({"User_Preference_Partner":user_profile.values()})
                        