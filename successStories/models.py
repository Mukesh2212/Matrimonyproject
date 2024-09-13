from django.db import models

# Create your models here.
class SuccessStory(models.Model):
    Title = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    Description = models.CharField(max_length=222222222, null = True, blank = True, default = None)
    image = models.ImageField(upload_to='success_stories', null = True, blank = True, default = None)
    date = models.DateField()
