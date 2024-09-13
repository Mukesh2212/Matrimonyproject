from django.db import models


# Create your models here.
class EducationDetail(models.Model):
    qualification = models.CharField(max_length=150,null=False,blank=False)
    occupations = models.CharField(max_length=150,null=False,blank=False)
    occupation_details = models.CharField(max_length=150,null=False,blank=False)
    annual_income = models.CharField(max_length=150,null=False,blank=False)
    employed_in = models.CharField(max_length=150,null=False,blank=False)
    working_location = models.CharField(max_length=150,null=False,blank=False)
    special_cases = models.CharField(max_length=150,null=False,blank=False)
    