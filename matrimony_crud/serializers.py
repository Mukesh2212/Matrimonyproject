from rest_framework import serializers 
from matrimony_crud.models import *
from MutualProfile.models import * 
from educationdetails.serializers import * 
from familydetails.serializers import * 
from horoscopedetails.serializers import * 
from basicinformationpage.serializers import * 

class HolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolaModel
        fields = "__all__"


class SixImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolaSixPhoto 
        fields = "__all__"


class IdProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdProof
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentAddress 
        fields = "__all__"

class CompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompatibilityMatch
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSection
        fields = "__all__"

class ProfileCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCompletes
        fields = "__all__"


class UserCompatibilityMatchSerializer(serializers.ModelSerializer):
    basic_information = serializers.SerializerMethodField()
    education_details = serializers.SerializerMethodField()
    family_details = serializers.SerializerMethodField()
    horoscope_details = serializers.SerializerMethodField()
    # partner_preference_details = serializers.SerializerMethodField()

    class Meta:
        model = UserCompatibilityMatch
        fields = ['id','user','How_often_do_you_go_out','How_would_you_describe_your_clothes',
        'How_do_you_spend_your_free_time','How_many_times_do_you_visit_salon_or_beauty_parlour',
        'How_many_times_do_you_go_out_drinking_or_in_a_pub','What_would_you_choose_for_a_romantic_date_with_your_partner',
        'Which_social_platform_do_you_use_Most','Do_you_like_shopping','Preferences_while_traveling',
        'Which_personality_are_you','created_at','basic_information','education_details','family_details','horoscope_details']

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
        

        


