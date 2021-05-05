from django.shortcuts import render
from mainapp.models import Product


def main(request):
    products = Product.objects.all()[:4]

    main_menu = {'links': [
        {'href': 'index', 'name': 'главная'},
        {'href': 'mainapp:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ],
        'topic': 'тренды',
        'heading': 'удобные стулья',
        'products': products,

    }
    return render(request, 'index.html', context=main_menu)


def products(request):
    main_menu = {'links': [
        {'href': 'index', 'name': 'главная'},
        {'href': 'mainapp:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]}
    return render(request, 'products.html', context=main_menu)


def contact(request):
    main_menu = {'links': [
        {'href': 'index', 'name': 'главная'},
        {'href': 'mainapp:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ],
        'heading': 'наши контакты'
    }
    return render(request, 'contact.html', context=main_menu)
