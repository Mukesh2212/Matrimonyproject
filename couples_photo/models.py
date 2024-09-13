from django.db import models
from django.contrib.auth.models import User


class CouplesPhoto(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True) 
    couple_photo_one = models.FileField(upload_to='couples/',null=True,blank=True)
    couple_photo_two = models.FileField(upload_to='couples/',null=True,blank=True)
    couple_photo_three = models.FileField(upload_to='couples/',null=True,blank=True)
    couple_photo_four = models.FileField(upload_to='couples/',null=True,blank=True)
    couple_photo_five = models.FileField(upload_to='couples/',null=True,blank=True)
    couple_photo_six = models.FileField(upload_to='couples/',null=True,blank=True)
    


