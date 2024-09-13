from django.db import models

# Create your models here.
class Contact(models.Model):
    Mobile_Number = models.CharField(max_length=255,null=False,blank=False)
    Alternative_Mobile_Number = models.CharField(max_length=255,null=False,blank=False)
    Convinient_Time_To_Call = models.CharField(max_length=255,null=False,blank=False)
    Email = models.EmailField(max_length=255, blank=False, null=False)
    Show_Permanent_Address = models.CharField(max_length=255,null=False,blank=False)
    Show_Working_Address = models.CharField(max_length=255,null=False,blank=False)
   


