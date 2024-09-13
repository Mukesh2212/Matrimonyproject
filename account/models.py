from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date
#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, name, tc, phoneNumber,password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          tc=tc,
          phoneNumber=phoneNumber,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, tc, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email,
          password=password,
          name=name,
          phoneNumber="909090909090",
          tc=tc,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}

class User(AbstractBaseUser):
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  name = models.CharField(max_length=200,null=True,blank=True)
  tc = models.BooleanField(null=True,blank=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.CharField(max_length=150,null=False,blank=False ,default=date.today)
  phoneNumber=models.CharField(max_length=2322,null=False,default=False)
  updated_at = models.DateTimeField(auto_now=True)
  auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
#   otp = models.CharField(max_length=6,null=True,blank=True)
  ########## new field ##########
 

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'tc']

  def str(self):
      return self.email

  def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }   

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin