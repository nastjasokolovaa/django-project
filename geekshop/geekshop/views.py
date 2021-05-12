from django.shortcuts import render
from mainapp.models import Product


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]

    links_menu = {'links': [
        {'href': 'index', 'name': 'главная'},
        {'href': 'mainapp:products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ],
        'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
        'topic': 'тренды',
        'heading': 'удобные стулья',
        'products': products,
        'title': title
    }
    return render(request, 'index.html', context=links_menu)


def contact(request):
    title = 'контакты'

    links_menu = {'links': [
        {'href': 'index', 'name': 'главная'},
        {'href': 'mainapp:products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ],
        'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
        'heading': 'наши контакты',
        'title': title
    }
    return render(request, 'contact.html', context=links_menu)
