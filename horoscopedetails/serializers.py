from rest_framework import serializers
from .models import *

class HoroscopeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoroscopeDetails
        fields = '__all__'