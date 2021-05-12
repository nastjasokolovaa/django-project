from django.shortcuts import render
from django.shortcuts import get_object_or_404
from mainapp.models import ProductCategory, Product


def products(request, pk=None):
    title = 'продукты'

    categories = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category_id__pk=pk).order_by('price')
        context = {'links': [
            {'href': 'index', 'name': 'главная'},
            {'href': 'mainapp:products', 'name': 'продукты'},
            {'href': 'contact', 'name': 'контакты'},
        ],
            'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
            'title': title,
            'categories': categories,
            'category': category,
            'products': products,
            }
        return render(request, 'products_list.html', context=context)
    else:
        links_menu = {'links': [
                {'href': 'index', 'name': 'главная'},
                {'href': 'mainapp:products', 'name': 'продукты'},
                {'href': 'contact', 'name': 'контакты'},
            ],
                'auth': [{'href': 'auth:edit', 'name': 'пользователь'}],
                'categories': categories,
                'title': title,
            }
        return render(request, 'products.html', context=links_menu)
