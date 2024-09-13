from django.db import models

# Create your models here.
class Familydetails(models.Model):
    CHOICE = (
        ('My parents will stay with me after marriage', 'My parents will stay with me after marriage'), 
        ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'),
        ('Dont wish to specify', 'Dont wish to specify'),
    )
    family_values = models.CharField(max_length=150,null=False,blank=False)
    family_type = models.CharField(max_length=150,null=False,blank=False)
    family_status = models.CharField(max_length=150,null=False,blank=False)
    no_of_brothers = models.CharField(max_length=150,null=False,blank=False,default='null')
    no_of_brothers_married = models.CharField(max_length=150,null=False,blank=False,default='null')
    no_of_sisters = models.CharField(max_length=150,null=False,blank=False,default='null')
    no_of_sisters_married = models.CharField(max_length=150,null=False,blank=False,default='null')
    mother_tounge = models.CharField(max_length=150,null=False,blank=False)
    father_name = models.CharField(max_length=150,null=False,blank=False,default='null')
    father_occupation = models.CharField(max_length=150,null=False,blank=False,default='null')
    mother_name = models.CharField(max_length=150,null=False,blank=False,default='null')
    mother_occupation = models.CharField(max_length=150,null=False,blank=False,default='null')
    family_wealth = models.CharField(max_length=150,null=False,blank=False,default='null')
    about_family = models.CharField(max_length=150,null=False,blank=False)
    options = models.CharField(choices=CHOICE,max_length=255)
