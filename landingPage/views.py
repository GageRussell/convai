from django.shortcuts import render
from django.http import HttpResponse
from djongo import models
objects = models.DjongoManager()
from .models import Convai
import datetime
# Create your views here.

def index(request):
    return render(request, "index.html")

# def email(request):
#
#     # TODO - pass data from webpage to function
#     #New Row
#     new_user = Convai.objects.create(email='grussell')
#     #update existing
#     new_user = Convai.objects.get(email='grussell')
#     new_user.email = 'colin'
#     new_user.save()
#     return HttpResponse("Success!")


def chat(request):
    return render(request, 'chat.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })