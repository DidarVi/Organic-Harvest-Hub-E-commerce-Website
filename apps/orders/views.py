from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def checkout(request):
    return HttpResponse("Checkout page")

def order_history(request):
    return HttpResponse("User's order history")
