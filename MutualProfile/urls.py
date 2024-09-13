from django.contrib import admin
from django.urls import path
from MutualProfile.views import *


urlpatterns = [
    path('mutualprofile/', MutualMatchesAPIView.as_view()),
    path('mutualprofile/<int:pk>/', MutualMatchesAPIView.as_view()),
]