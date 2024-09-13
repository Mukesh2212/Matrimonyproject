from django.shortcuts import render
from couples_photo.models import CouplesPhoto
from couples_photo.serializers import * 
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class CouplesPhotoApiview(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = CouplesPhotoSerializers(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response({'couples phot':'couples photo has created successfully','Couple Image':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self,request,pk=None,format=None):
        id = pk 
        if id is not None:
            couple_pic = CouplesPhoto.objects.get(id=id)
            serializer = CouplesPhotoSerializers(couple_pic) 
            return Response({'All couples photo':serializer.data}) 
        couple_pic = CouplesPhoto.objects.all()
        serializer = CouplesPhotoSerializers(couple_pic,many=True) 
        return Response({"All couples photo":serializer.data})
    
    def put(self,request,pk,format=None):
        couple_photo = CouplesPhoto.objects.get(id = pk)
        serializer = CouplesPhotoSerializers(couple_photo,data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Updated Data':serializer.data}) 
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        couple_photo = CouplesPhoto.objects.get(id = pk)
        couple_photo.delete()
        return Response({'Message':'Data has deleted successfully'})
 
class TokenObtainPairAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)