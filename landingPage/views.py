from django.shortcuts import render
from django.http import HttpResponse
from djongo import models
objects = models.DjongoManager()
from .models import Convai
import datetime
# Create your views here.

def index(request):
    return render(request, "index.html")

def email(request):
    #New Row
    new_user = Convai.objects.create(email='grussell')
    #update existing
    new_user = Convai.objects.get(email='grussell')
    new_user.email = 'colin'
    new_user.save()
    return HttpResponse("Success!")
