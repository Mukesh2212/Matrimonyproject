from django.contrib import admin
from otp_reg.models import *

class OTPVerifiactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'otp', 'is_verfied')


admin.site.register(CustomUser)

admin.site.register(OTPVerifiaction, OTPVerifiactionAdmin)

