from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('profile/register/', ProfileRegister.as_view(), name='book-list'),
    path('profile_register/<int:pk>/', Profile_registerUpdateDeleteView.as_view(), name='book-detail'),
    path('profile/', ProfileCompletionsAPIView.as_view()),
    path('profile/<int:pk>/', ProfileCompletionsAPIView.as_view()),
    path('mutual/profileapi/<int:pk>/', MutualProfileMatching.as_view()),
    path('mutual/profileapi/', MutualProfileMatching.as_view()),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
