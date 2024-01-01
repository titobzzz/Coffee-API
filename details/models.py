from django.db import models

# Create your models here.


class profile(models.Model):

    gender= models.CharField(max_length=100,blank=False, null=False)
    giturl = models.TextField(max_length=100,blank=False, null=False)
    name= models.CharField(max_length=100,blank=False, null=False)