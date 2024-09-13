from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from basicinformationpage.models import *
from basicinformationpage.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BasicInformationList(APIView):
    def get(self, request, format=None):
        Basic = BasicInformation.objects.all()
        serializer = BasicinformationSerializer(Basic, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BasicinformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BasicInformationDetail(APIView):
    def get_object(self, pk):
        try:
            return BasicInformation.objects.get(pk=pk)
        except BasicInformation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        BasicInformation = self.get_object(pk)
        serializer = BasicinformationSerializer(BasicInformation)
        return Response(serializer.data)

    def  put(self, request, pk, format=None):
        BasicInformation = self.get_object(pk)
        serializer = BasicinformationSerializer(BasicInformation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # Return the updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        BasicInformation = self.get_object(pk)
        BasicInformation.delete()
        response_data = {"message": "Basic Information has been deleted successfully."}
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        
     
        

# class BasicInformationAPIView(APIView):
#     def get(self, request , pk=None,format=None):
#         id = pk 
#         if id is not None:
#             profile_ojb = BasicProfileCompletionApi.objects.get(id=id)
#             serializer = BasicInformationCompletionSerializer(profile_ojb)
#             return Response(serializer.data)
#         profiles = BasicProfileCompletionApi.objects.all()
#         serializer = BasicInformationCompletionSerializer(profiles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BasicInformationCompletionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)