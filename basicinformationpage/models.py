from django.db import models

# Create your models here.
class BasicInformation(models.Model):
    Name = models.CharField(max_length=255, blank=False, null=False)
    Surname = models.CharField(max_length=255, blank=False, null=False)
    Email = models.EmailField(max_length=255, blank=False, null=False)
    Mobile_Number = models.CharField(max_length=255, blank=False, null=False)
    D_O_B = models.CharField(max_length=255, blank=False, null=False)
    Age = models.CharField(max_length=255, blank=False, null=False)
    Height = models.CharField(max_length=255, blank=False, null=False)
    Blood_Group = models.CharField(max_length=255, blank=False, null=False)
    Gender = models.CharField(max_length=255, blank=False, null=False)
    religion = models.CharField(max_length=255,blank=False,null=False)
    profile_created_By = models.CharField(max_length=255,null=False,blank=False)
    marital_status = models.CharField(max_length=255,null=False,blank=False)
    your_religion = models.CharField(max_length=255,null=False,blank=False)
    your_caste = models.CharField(max_length=255,null=False,blank=False)
    sub_caste = models.CharField(max_length=255,null=False,blank=False)
    about_yourself = models.CharField(max_length=255,null=False,blank=False)


