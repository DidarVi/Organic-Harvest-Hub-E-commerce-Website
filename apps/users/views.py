from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse("User registration page")

def login_view(request):
    return HttpResponse("User login page")

def logout_view(request):
    return HttpResponse("User logout page")
