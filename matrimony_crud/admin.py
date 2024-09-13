from django.contrib import admin
from matrimony_crud.models import *

@admin.register(HolaModel)
class HolaModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','profile_pic']

@admin.register(HolaSixPhoto)
class HolaSixPhotoAdmin(admin.ModelAdmin):
    list_display = ['id','user','pic1','pic2','pic3','pic4','pic5','pic6']

@admin.register(IdProof)
class IdProofAdmin(admin.ModelAdmin):
    list_display = ['id','id_proof','passport_size_photo'] 

@admin.register(DocumentAddress)
class DocumentAddressAdmin(admin.ModelAdmin):
    list_display = ['id','address_id','certificates']

@admin.register(CompatibilityMatch)
class CompatibilityMatchAdmin(admin.ModelAdmin):
    list_display = ['id','How_often_do_you_go_out','How_would_you_describe_your_clothes',
                    'How_do_you_spend_your_free_time','How_many_times_do_you_visit_salon_or_beauty_parlour',
                    'How_many_times_do_you_go_out_drinking_or_in_a_pub','What_would_you_choose_for_a_romantic_date_with_your_partner',
                    'Which_social_platform_do_you_use_Most','Do_you_like_shopping',
                    'Preferences_while_traveling','Which_personality_are_you']
    

@admin.register(ReviewSection)
class ReviewSectionAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','rating','descriptions','user_profile','profile_image']


@admin.register(ProfileCompletes)
class ProfileCompleteAdmin(admin.ModelAdmin):
    list_display = ['id','profile_photo','basic_details_completed','education_details_completed','horoscope_details_completed',
                    'family_details_completed','partner_preference_details_completed','habits_details_completed','hobbies_details_completed','interest_details_completed']
    

@admin.register(UserCompatibilityMatch)
class UserCompatibilityMatchAdmin(admin.ModelAdmin):
    list_display = ['id','How_often_do_you_go_out','How_would_you_describe_your_clothes',
                    'How_do_you_spend_your_free_time','How_many_times_do_you_visit_salon_or_beauty_parlour',
                    'How_many_times_do_you_go_out_drinking_or_in_a_pub','What_would_you_choose_for_a_romantic_date_with_your_partner',
                    'Which_social_platform_do_you_use_Most','Do_you_like_shopping',
                    'Preferences_while_traveling','Which_personality_are_you','created_at']
    