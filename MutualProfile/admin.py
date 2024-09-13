from django.contrib import admin
from MutualProfile.models import * 

@admin.register(UserProfileMutual)
class UserProfileMutualAdmin(admin.ModelAdmin):
    list_display = ['id','user','looking_for','age_from','age_to','height_from','heigiht_to','rellgion','caste',
                    'complexion','residency_status','country','education','occupation','partner_expectations','created_at']
    
    list_filter = ('created_at',)

# @admin.register(PartnerPreferenceMutual)
# class PartnerPreferenceMutualAdmin(admin.ModelAdmin):
#     list_display = ['id','user','looking_for','age_from','age_to','height_from','height_to','relligion','caste'
#                     ,'complexion','residency_status','country','education','occupation','partner_expectations']

    
admin.site.register(BasicDetails)
admin.site.register(EducationDetails)
admin.site.register(Familydetail)
admin.site.register(HoroscopeDetail)