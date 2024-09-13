from rest_framework import serializers
from .models import *

class PartnerPrefarenceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerPrefarenceDetails
        fields = '__all__'