"""
URL configuration for Matrimonybackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('api/otp_reg/', include('otp_reg.urls')),
    path('api/BasicinformationPageapi/', include('basicinformationpage.urls')),
    path('api/EducationDetails/', include('educationdetails.urls')),
    path('api/Familydeatilsapi/', include('familydetails.urls')),
    path('api/Horoscopeapi/', include('horoscopedetails.urls')),
    path('api/partnerapi/', include('partnerpreferencedetails.urls')),
    path('api/profileapi/', include('profileapi.urls')),
    path('api/Searchapi/', include('GlobalSearch.urls')),
    path('api/Successtoriesapi/', include('successStories.urls')),
    path('api/Contackdetailsapi/', include('ContactUs.urls')),
    path('api/crud/',include('matrimony_crud.urls')),
    path('api/crud/',include('couples_photo.urls')),
    path('api/mutualprofiles/',include('MutualProfile.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#   https://github.com/HolaReact/Matrimonybackend.git

# git remote add origin "https://github.com/HolaReact/Matrimonybackend.git"












