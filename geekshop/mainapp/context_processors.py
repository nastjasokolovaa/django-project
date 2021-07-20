from django.conf import settings
from django.core.cache import cache

from authapp.models import ShopUser
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def basket(request):
    basket_list = []
    if request.user.is_authenticated:
        basket_list = Basket.objects.filter(user=request.user)
    return {
        'basket': basket_list
    }


def get_category_menu():
    if settings.LOW_CACHE:
        key = 'category_menu'
        category_menu = cache.get(key)
        if category_menu is None:
            category_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, category_menu)
        return category_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_links():
    links_ = [{'href': 'index', 'name': 'главная'},
              {'href': 'mainapp:products', 'name': 'продукты'},
              {'href': 'contact', 'name': 'контакты'}]
    return links_


def get_auth(request):
    name = ShopUser.objects.filter(username=request.user.username).first()
    auth_ = [{'href': 'auth:edit', 'name': name}]
    return auth_


def get_links_menu(request, title, heading=None):
    products = Product.objects.all()[:4]
    links_menu = {
        'links': list(get_links()),
        'auth': list(get_auth(request)),
        'topic': 'тренды',
        'heading': heading,
        'title': title,
        'products': products,
        'categories': get_category_menu(),
    }
    return links_menu
