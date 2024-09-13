from django.db import models
from django.contrib.auth.models import User


class UserProfileMutual(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    looking_for = models.CharField(max_length=255,choices=GENDER_CHOICES,null=True,blank=True)
    age_from = models.CharField(max_length=255,null=False,blank=False)
    age_to = models.CharField(max_length=255,null=False,blank=False)
    height_from = models.CharField(max_length=255,null=False,blank=False)
    heigiht_to = models.CharField(max_length=255,null=False,blank=False)
    rellgion = models.CharField(max_length=255,null=False,blank=False)
    caste = models.CharField(max_length=255,null=False,blank=False)
    complexion = models.CharField(max_length=255,null=False,blank=False)
    residency_status = models.CharField(max_length=255,null=False,blank=False)
    country = models.CharField(max_length=255,null=False,blank=False)
    education = models.CharField(max_length=255,null=False,blank=False)
    occupation = models.CharField(max_length=255,null=False,blank=False)
    partner_expectations = models.CharField(max_length=255,null=False,blank=False)
    created_at = models.DateField(auto_created=True, null=True,blank=True)
    
# class PartnerPreferenceMutual(models.Model):
#     user = models.ForeignKey(UserProfileMutual, on_delete=models.CASCADE)
#     looking_for = models.CharField(max_length=255,null=False,blank=False)
#     age_from = models.CharField(max_length=255,null=False,blank=False)
#     age_to = models.CharField(max_length=255,null=False,blank=False)
#     height_from = models.CharField(max_length=255,null=False,blank=False)
#     height_to = models.CharField(max_length=255,null=False,blank=False)
#     relligion = models.CharField(max_length=255,null=False,blank=False)
#     caste = models.CharField(max_length=255,null=False,blank=False)
#     complexion = models.CharField(max_length=255,null=False,blank=False)
#     residency_status = models.CharField(max_length=255,null=False,blank=False)
#     country = models.CharField(max_length=255,null=False,blank=False)
#     education = models.CharField(max_length=255,null=False,blank=False)
#     occupation = models.CharField(max_length=255,null=False,blank=False)
#     partner_expectations = models.CharField(max_length=255,null=False,blank=False)
    
class BasicDetails(models.Model):
    user_basic_details = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_basic_details')
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


class EducationDetails(models.Model):
    user_education_details = models.OneToOneField(User,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=150,null=False,blank=False)
    occupations = models.CharField(max_length=150,null=False,blank=False)
    occupation_details = models.CharField(max_length=150,null=False,blank=False)
    annual_income = models.CharField(max_length=150,null=False,blank=False)
    employed_in = models.CharField(max_length=150,null=False,blank=False)
    working_location = models.CharField(max_length=150,null=False,blank=False)
    special_cases = models.CharField(max_length=150,null=False,blank=False) 
    

class Familydetail(models.Model):
    CHOICE = (
        ('My parents will stay with me after marriage', 'My parents will stay with me after marriage'), 
        ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'),
        ('Dont wish to specify', 'Dont wish to specify'),
    )
    user_family_details = models.OneToOneField(User,on_delete=models.CASCADE)
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



class HoroscopeDetail(models.Model):
    user_horoscope_details = models.OneToOneField(User,on_delete=models.CASCADE)
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