from rest_framework import serializers
from .models import *

class FamilydetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familydetails
        fields='__all__'