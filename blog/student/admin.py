from django.contrib import admin
from django import forms
from django.forms import ModelForm

from student.models import registration, sdata
# Register your models here.
admin.site.register(registration)
admin.site.register(sdata)
