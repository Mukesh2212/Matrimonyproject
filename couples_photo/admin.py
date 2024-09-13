from django.contrib import admin

from couples_photo.models import * 

@admin.register(CouplesPhoto)
class CouplesPhotoAdmin(admin.ModelAdmin):
    list_display = ['id','couple_photo_one','couple_photo_two','couple_photo_three','couple_photo_four',
    'couple_photo_five','couple_photo_six']
    

