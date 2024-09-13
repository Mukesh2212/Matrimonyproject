
from django.contrib import admin
from django.urls import path
from matrimony_crud import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('holaapi/',views.HolaApi.as_view()),
    path('holaapi/<int:pk>/',views.HolaApi.as_view()),
    path('siximages/',views.SixImageApi.as_view()),
    path('siximages/<int:pk>/',views.SixImageApi.as_view()),
    path('reviewapi/',views.ReviewsApi.as_view()),
    path('reviewapi/<int:pk>/',views.ReviewsApi.as_view()),
    path('idproofapi/',views.IdProofApiview.as_view()),
    path('idproofapi/<int:pk>/',views.IdProofApiview.as_view()),
    path('documentapi/',views.DocumentApiview.as_view()),
    path('documentapi/<int:pk>/',views.DocumentApiview.as_view()),
    path('compatibilityapi/',views.CompatibilityApiview.as_view()),
    path('compatibilityapi/<int:pk>/',views.CompatibilityApiview.as_view()),
    path('usercompatibilityapimatch/',views.CompatibilityMatchuser.as_view()),
    path('usercompatibilityapimatch/<int:pk>/',views.CompatibilityMatchuser.as_view()),
    path('profilecompleteapi/',views.ProfileCompletationsApiview.as_view()),
    path('profilecompleteapi/<int:pk>/',views.ProfileCompletationsApiview.as_view()),
   

] 