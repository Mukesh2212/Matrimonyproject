from rest_framework import serializers
from .models import *


class EducationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetail
        fields = '__all__'