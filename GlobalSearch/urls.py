from django.urls import path
from .views import  *
from account.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('SearchAPIViewlist/', SearchAPIViewlist.as_view(), name='SearchAPIViewlist'),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)