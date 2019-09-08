from django.db import models


# Create your models here.

class registration(models.Model):
    studentname = models.CharField(max_length=50)
    collegename  =  models.CharField(max_length=50)
    branch   =  models.CharField(max_length=50)
