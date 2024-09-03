from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def product_list(request):
    return HttpResponse("List of products")

def product_detail(request, product_id):
    return HttpResponse(f"Detail of product {product_id}")
