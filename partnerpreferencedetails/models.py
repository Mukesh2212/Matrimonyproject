from django.db import models

# Create your models here.
class PartnerPrefarenceDetails(models.Model): 
    looking_for = models.CharField(max_length=255,null=False,blank=False)
    age_from = models.CharField(max_length=255,null=False,blank=False)
    age_to = models.CharField(max_length=255,null=False,blank=False)
    height_from = models.CharField(max_length=255,null=False,blank=False)
    height_to = models.CharField(max_length=255,null=False,blank=False)
    relligion = models.CharField(max_length=255,null=False,blank=False)
    caste = models.CharField(max_length=255,null=False,blank=False)
    complexion = models.CharField(max_length=255,null=False,blank=False)
    residency_status = models.CharField(max_length=255,null=False,blank=False)
    country = models.CharField(max_length=255,null=False,blank=False)
    education = models.CharField(max_length=255,null=False,blank=False)
    occupation = models.CharField(max_length=255,null=False,blank=False)
    partner_expectations = models.CharField(max_length=255,null=False,blank=False)
   
    
    
    
   
    
    


