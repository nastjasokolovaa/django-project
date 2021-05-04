from django.shortcuts import render


def products(request):
    links_menu = {'links': [
        {'href': 'mainapp:index', 'name': 'все'},
        {'href': 'mainapp:index', 'name': 'дом'},
        {'href': 'mainapp:index', 'name': 'офис'},
        {'href': 'mainapp:index', 'name': 'модерн'},
        {'href': 'mainapp:index', 'name': 'классика'}
    ],
        'menu': [
        {'href': 'index', 'name': 'главная'},
        {'href': 'mainapp:index', 'name': 'продукты'},
        {'href': 'contact', 'name': 'контакты'},
    ]}

    return render(request, 'products.html', context=links_menu)
