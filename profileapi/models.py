from unicodedata import category
from django.db import models
# from embed_video.fields import EmbedVideoField
from account.models import User

# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh' , 'Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
              ('Goa','Goa'),
    ('Gujrat','Gujrat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharastra','Maharastra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telengana','Telengana'),
    ('Tripura','Tripura'),
    ('Uttarkhand','Uttarkhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
    )



import datetime
class Profile(models.Model):
    image = models.FileField(upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=150,null = True, blank = True)
    email = models.CharField(max_length=150,null = True, blank = True)
    PhoneNumber = models.CharField(max_length=25,null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    state = models.CharField(choices=STATE_CHOICES,max_length=50,null = True, blank = True)
    city = models.CharField(max_length=50,null = True, blank = True)
    zipcode = models.CharField(max_length=6,null = True, blank = True)
    date = models.CharField(max_length=10,null = True, blank = True ,default=datetime.datetime.now().strftime('%Y-%m-%d'))
    age = models.IntegerField(null = True, blank = True, default = None)
    gender = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    religion = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    caste = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    height = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    education = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    occupation = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    income = models.IntegerField(null = True, blank = True, default = None)

    def __str__(self):
        return self.name



class ProfileCompletionsApi(models.Model):
    basic_information = models.IntegerField(null=True,blank=True) 
    profile_photo = models.IntegerField(null=True,blank=True) 
    education_details = models.IntegerField(null=True,blank=True) 
    horoscope_details = models.IntegerField(null=True,blank=True) 
    partner_prefrence = models.IntegerField(null=True,blank=True) 
    family_details  = models.IntegerField(null=True,blank=True) 
    habits = models.IntegerField(null=True,blank=True) 
    hobbies = models.IntegerField(null=True,blank=True) 
    interest = models.IntegerField(null=True,blank=True) 

