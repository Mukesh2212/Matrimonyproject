from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True,many=True)
    
    class Meta:
        model = Profile
        fields = ['id','image','user','name','email','PhoneNumber','address','state','city','zipcode','date','age',
        'gender','religion','caste','height','education','occupation','income']
        # read_only_fields = ('user',)


class ProfileCompletionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCompletionsApi
        fields = "__all__"

    