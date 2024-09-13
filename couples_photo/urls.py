from django.contrib import admin
from django.urls import path
from couples_photo.views import * 
from rest_framework_simplejwt.views import TokenObtainSlidingView,TokenRefreshSlidingView
    
    


urlpatterns = [
    path('couples/photo/',CouplesPhotoApiview.as_view()),
    path('couples/photo/<int:pk>/',CouplesPhotoApiview.as_view()),
    path('token/', TokenObtainPairAPIView.as_view(), name='token-obtain-pair'),
   


]