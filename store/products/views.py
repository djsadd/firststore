from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'title': 'Store',
               }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'products - каталог',
        'products': [
            {'url': '/static/vendor/img/products/Adidas-hoodie.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00 руб.',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},

            {'url': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00 руб.',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},

            {'url': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'name': 'Худи черного цвета с монограммами adidas Originals',
             'price': '6 090,00 руб.',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},

        ]
               }
    return render(request, 'products/products.html', context=context)
