from rest_framework import serializers 
from couples_photo.models import * 

class CouplesPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = CouplesPhoto 
        fields = "__all__"