from django.shortcuts import render
from mainapp.models import ProductCategory


def products(request):
    categories = ProductCategory.objects.all()[:4]

    links_menu = {'links': [
        {'href': 'index', 'name': 'главная'},
        {'href': 'mainapp:products', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ],
        'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
        'categories': categories,
    }

    return render(request, 'products.html', context=links_menu)
