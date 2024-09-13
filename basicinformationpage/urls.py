from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('BasicInformationList/', BasicInformationList.as_view()),
    path('BasicInformationList/<int:pk>/', BasicInformationDetail.as_view()),
   

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 