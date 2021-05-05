from django.shortcuts import render
from mainapp.models import ProductCategory


def products(request):
    categories = ProductCategory.objects.all()[:4]

    # links = {'links': [
    #     {'href': 'mainapp:index', 'name': 'все'},
    #     {'href': 'mainapp:index', 'name': 'дом'},
    #     {'href': 'mainapp:index', 'name': 'офис'},
    #     {'href': 'mainapp:index', 'name': 'модерн'},
    #     {'href': 'mainapp:index', 'name': 'классика'}
    # ]}

    links_menu = {'menu': [
        {'href': 'index', 'name': 'главная'},
        {'href': 'mainapp:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ],
        'categories': categories,
    }

    return render(request, 'products.html', context=links_menu)
