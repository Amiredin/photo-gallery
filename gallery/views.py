from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def welcome(request):
    image = image.get_images()
    context= {'images':images}
    return render (request, 'index.html')