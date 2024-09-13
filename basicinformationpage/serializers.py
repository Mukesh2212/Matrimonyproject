from rest_framework import serializers
from basicinformationpage.models import *

class BasicinformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = '__all__'


