from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def product(request):
    return render (request,'products/product.html',{'pro':Product.objects.get(name='oppo')})


def products(request):
    pro=Product.objects.all()
    x={'pro':pro.filter()}
    return render (request,'products/products.html',x)