import random

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def get_products():
    return Product.objects


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return ''


def get_hot_product():
    products = get_products().all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_products):
    same_products = get_products().filter(category=hot_products.category).exclude(pk=hot_products.pk)[:3]

    return same_products


def get_links():
    links_ = [{'href': 'index', 'name': 'главная'},
              {'href': 'mainapp:products', 'name': 'продукты'},
              {'href': 'contact', 'name': 'контакты'}]
    return links_


def products(request, pk=None, page=1):
    title = 'продукты'
    basket = get_basket(request.user)
    categories = ProductCategory.objects.all()
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    links_menu = {
        'links': list(get_links()),
        'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
        'categories': categories,
        'title': title,
        'basket': basket,
    }
    if pk is not None:
        if pk == 0:
            products = get_products().all().order_by('price')
            category = {'name': 'все', 'pk': '0'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = get_products().filter(category_id__pk=pk).order_by('price')

        paginator = Paginator(products, 2)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(1)

        links_menu.update(
            {
                'category': category,
                'products': products_paginator,
            }
        )
        return render(request, 'products_list.html', context=links_menu)
    else:
        links_menu.update(
            {
                'hot_product': hot_product,
                'same_products': same_products,
            }
        )
        return render(request, 'products.html', context=links_menu)


@login_required
def product(request, pk):
    title = 'Страница продукта'
    categories = ProductCategory.objects.all()
    basket = get_basket(request.user)
    pk_product = get_object_or_404(Product, pk=pk)
    same_products = get_same_products(pk_product)
    links_menu = {
        'links': list(get_links()),
        'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
        'categories': categories,
        'title': title,
        'basket': basket,
        'pk_product': pk_product,
        'same_products': same_products,
    }

    return render(request, 'product.html', context=links_menu)
