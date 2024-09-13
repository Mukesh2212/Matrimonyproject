from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Familydetails/', FamilydetailsList.as_view()),
    path('Familydetails/<int:pk>/', Familydetailsview.as_view()),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)