from django.shortcuts import render
from products.models import *

# Create your views here.


def index(request):
    context = {
        'title': 'Store',
               }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'products - каталог',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all(),
               }
    return render(request, 'products/products.html', context=context)
