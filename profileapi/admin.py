from django.contrib import admin
from profileapi.models import *
# Register your models here.

# admin.site.register(Profile) 



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','image','user','name','email','PhoneNumber','address','state','city','zipcode','date',
    'age','gender','religion','caste','height','education','occupation','income']
    


    
@admin.register(ProfileCompletionsApi)
class ProfileCompletionApiAdmin(admin.ModelAdmin):
    list_display = ['id','basic_information','profile_photo','education_details','horoscope_details',
    'partner_prefrence','family_details','habits','hobbies','interest']