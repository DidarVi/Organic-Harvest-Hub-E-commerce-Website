from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def cart_detail(request):
    return HttpResponse("Shopping cart details")

def add_to_cart(request, product_id):
    return HttpResponse(f"Added product {product_id} to cart")

def remove_from_cart(request, product_id):
    return HttpResponse(f"Removed product {product_id} from cart")

