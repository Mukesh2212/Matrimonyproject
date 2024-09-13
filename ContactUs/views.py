from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework import generics
from .models import *
from .serializers import *

class Contact_register(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUsSerializer

class Contact_registerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUsSerializer

