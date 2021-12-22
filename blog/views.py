from django.shortcuts import render, HttpResponse
from django.urls.conf import re_path

# Create your views here.
def index(request):
    return HttpResponse("Blog Index")