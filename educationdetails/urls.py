from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('educationDetail/', EducationDetailList.as_view()),
    path('educationDetail/<int:pk>/', EducationDetailview.as_view()),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)