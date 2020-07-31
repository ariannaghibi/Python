from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# These functions return the appropriate response back to the website
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('Nothing new here 😭')
