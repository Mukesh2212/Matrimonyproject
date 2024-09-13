from sys import modules
from django.db import models
from django.contrib.auth.models import User 

class HolaModel(models.Model):
    user = models.CharField(max_length=20,null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True,null=True)


class HolaSixPhoto(models.Model):
    user = models.CharField(max_length=20,null=True,blank=True)
    pic1 = models.ImageField(upload_to='six_images',null=True,blank=True)
    pic2 = models.ImageField(upload_to='six_images',null=True,blank=True)
    pic3 = models.ImageField(upload_to='six_images',null=True,blank=True)
    pic4 = models.ImageField(upload_to='six_images',null=True,blank=True)
    pic5 = models.ImageField(upload_to='six_images',null=True,blank=True)
    pic6 = models.ImageField(upload_to='six_images',null=True,blank=True)
    

class IdProof(models.Model):
    id_proof = models.FileField(upload_to='id_proof',null=True,blank=True)
    passport_size_photo = models.ImageField(upload_to='passport_photo',null=True,blank=True)


class DocumentAddress(models.Model):
    address_id = models.FileField(upload_to='document',null=True,blank=True) 
    certificates = models.FileField(upload_to='documents',null=True,blank=True) 


class CompatibilityMatch(models.Model):
    How_often_do_you_go_out = models.CharField(max_length=222,blank=True,null=True) 
    How_would_you_describe_your_clothes = models.CharField(max_length=235,blank=True,null=True) 
    How_do_you_spend_your_free_time  = models.CharField(max_length=235,null=True,blank=True)
    How_many_times_do_you_visit_salon_or_beauty_parlour = models.CharField(max_length=235,null=True,blank=True)
    How_many_times_do_you_go_out_drinking_or_in_a_pub = models.CharField(max_length=235,null=True,blank=True) 
    What_would_you_choose_for_a_romantic_date_with_your_partner = models.CharField(max_length=234,null=True,blank=True) 
    Which_social_platform_do_you_use_Most = models.CharField(max_length=234,null=True,blank=True)
    Do_you_like_shopping = models.BooleanField(null=True,blank=True)
    Preferences_while_traveling = models.CharField(max_length=234,blank=True,null=True)
    Which_personality_are_you = models.CharField(max_length=234,null=True,blank=True)



class UserCompatibilityMatch(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    How_often_do_you_go_out = models.CharField(max_length=222,blank=True,null=True) 
    How_would_you_describe_your_clothes = models.CharField(max_length=235,blank=True,null=True) 
    How_do_you_spend_your_free_time  = models.CharField(max_length=235,null=True,blank=True)
    How_many_times_do_you_visit_salon_or_beauty_parlour = models.CharField(max_length=235,null=True,blank=True)
    How_many_times_do_you_go_out_drinking_or_in_a_pub = models.CharField(max_length=235,null=True,blank=True) 
    What_would_you_choose_for_a_romantic_date_with_your_partner = models.CharField(max_length=234,null=True,blank=True) 
    Which_social_platform_do_you_use_Most = models.CharField(max_length=234,null=True,blank=True)
    Do_you_like_shopping = models.BooleanField(null=True,blank=True)
    Preferences_while_traveling = models.CharField(max_length=234,blank=True,null=True)
    Which_personality_are_you = models.CharField(max_length=234,null=True,blank=True)
    created_at = models.DateField(auto_created=True, null=True,blank=True)

class ReviewSection(models.Model):
    user_profile = models.OneToOneField(HolaModel,on_delete=models.CASCADE,null=True,blank=True)
    name =  models.CharField(max_length=29,null=True, blank=True)
    email = models.EmailField(blank=True,null=True)
    rating = models.IntegerField(blank=True,null=True)
    descriptions = models.TextField(blank=True,null=True) 
    profile_image = models.ImageField(upload_to='review_images/', null=True, blank=True)


class ProfileCompletes(models.Model):
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    basic_details_completed = models.CharField(max_length=200,null=True,blank=True)
    education_details_completed = models.CharField(max_length=200,null=True,blank=True)
    horoscope_details_completed = models.CharField(max_length=200,null=True,blank=True)
    family_details_completed = models.CharField(max_length=200,null=True,blank=True)
    partner_preference_details_completed = models.CharField(max_length=200,null=True,blank=True)
    habits_details_completed = models.CharField(max_length=200,null=True,blank=True)
    hobbies_details_completed = models.CharField(max_length=200,null=True,blank=True)
    interest_details_completed = models.CharField(max_length=200,null=True,blank=True)



