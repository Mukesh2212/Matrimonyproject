from django.db import models

# Create your models here.
class HoroscopeDetails(models.Model):
    moon_sign = models.CharField(max_length=150,null=False,blank=False)
    star = models.CharField(max_length=150,null=False,blank=False)
    gotra = models.CharField(max_length=150,null=False,blank=False)
    manglik = models.CharField(max_length=150,null=False,blank=False)
    shani = models.CharField(max_length=150,null=False,blank=False)
    hororscope_match = models.CharField(max_length=150,null=False,blank=False)
    place_of_birth = models.CharField(max_length=150,null=False,blank=False)
    place_of_country = models.CharField(max_length=255,null=False,blank=False)
    hours = models.CharField(max_length=255,null=False,blank=False)
    minitues = models.CharField(max_length=255,null=False,blank=False)
    seconds = models.CharField(max_length=255,null=False,blank=False)
    am_pm = models.CharField(max_length=255,null=False,blank=False)
