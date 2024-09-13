from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('partnerprefarence/', partnerprefarencelist.as_view(), name='partnerprefarencelist'),
    path('partnerprefarence/<int:pk>/', partnerprefarenceView.as_view(), name='partnerprefarenceView'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)