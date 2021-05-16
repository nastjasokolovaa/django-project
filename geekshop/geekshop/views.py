from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return ''


def get_links():
    links_ = [{'href': 'index', 'name': 'главная'},
              {'href': 'mainapp:products', 'name': 'продукты'},
              {'href': 'contact', 'name': 'контакты'}]
    return links_


def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    basket = get_basket(request.user)
    links_menu = {
        'links': list(get_links()),
        'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
        'topic': 'тренды',
        'heading': 'удобные стулья',
        'products': products,
        'title': title,
        'basket': basket,
    }
    return render(request, 'index.html', context=links_menu)


def contact(request):
    title = 'контакты'
    basket = get_basket(request.user)
    links_menu = {
        'links': list(get_links()),
        'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
        'heading': 'наши контакты',
        'title': title,
        'basket': basket,
    }
    return render(request, 'contact.html', context=links_menu)
