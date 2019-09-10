from django.db import models


# Create your models here.

class registration(models.Model):
    studentname = models.CharField(max_length=50)
    collegename  =  models.CharField(max_length=50)
    branch   =  models.CharField(max_length=50)

class sdata(models.Model):
    sname = models.CharField(max_lenght=50)
    address = models.CharField(max_lengh=40)
    fathername = models.CharField(max_lenght=20)
    mothername = models.CharField(max_lenght=20)
    college = models.CharField(max_lengh=40)
    collegeid = models.IntegerField(max_length=10)
    department = models.CharField(max_length=10)



