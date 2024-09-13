from rest_framework import serializers 
from MutualProfile.models import * 
from educationdetails.models import * 
from basicinformationpage.serializers import * 
from basicinformationpage.models import * 
from educationdetails.serializers import * 
from familydetails.serializers import * 
from horoscopedetails.serializers import * 

class UserProfileSerializer(serializers.ModelSerializer):
    basic_information = serializers.SerializerMethodField()
    education_details = serializers.SerializerMethodField()
    family_details = serializers.SerializerMethodField()
    horoscope_details = serializers.SerializerMethodField()
    # partner_preference_details = serializers.SerializerMethodField()

    class Meta:
        model = UserProfileMutual
        fields = ['id','user','looking_for','age_from','age_to','height_from','heigiht_to','rellgion',
        'caste','complexion','residency_status','country','education','occupation','partner_expectations',
        'created_at','basic_information','education_details','family_details','horoscope_details']

    def get_basic_information(self, obj):
        try:
            basic_info = BasicDetails.objects.get(user_basic_details=obj.user)
            return BasicinformationSerializer(basic_info).data
        except Exception:
            return None

            
    def get_education_details(self, obj):
        try:
            basic_info = EducationDetails.objects.get(user_education_details=obj.user)
            return EducationDetailSerializer(basic_info).data
        except Exception:
            return None

    def get_family_details(self, obj):
        try:
            basic_info = Familydetail.objects.get(user_family_details=obj.user)
            return FamilydetailsSerializer(basic_info).data
        except Exception:
            return None


    def get_horoscope_details(self, obj):
        try:
            basic_info = HoroscopeDetail.objects.get(user_horoscope_details=obj.user)
            return HoroscopeDetailsSerializer(basic_info).data
        except Exception:
            return None
        

        


