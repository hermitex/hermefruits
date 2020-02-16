from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(http_request):
    products = Product.objects.all()
    return render(http_request,
                  "index.html",
                  {"products": products})

def new(http_request):
    return HttpResponse("New Product")
