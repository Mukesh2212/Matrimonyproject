from django.shortcuts import render
from rest_framework import viewsets
from .models import SuccessStory
from .serializers import SuccessStorySerializer


# Create your views here.

class SuccessStoryViewSet(viewsets.ModelViewSet):
    queryset = SuccessStory.objects.all()
    serializer_class = SuccessStorySerializer

