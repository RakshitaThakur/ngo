from django.shortcuts import render,redirect
from . forms import *
from . models import *


def registration(request):
    form=registration_form()
    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=registration_form()
    return render(request,'student/registration.html',{'forms':form})