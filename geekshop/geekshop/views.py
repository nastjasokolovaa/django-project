from django.shortcuts import render
from mainapp.context_processors import get_links_menu


def main(request):
    title = 'главная'
    heading = 'удобные стулья'
    links_menu = get_links_menu(request, title=title, heading=heading)

    return render(request, 'geekshop/index.html', context=links_menu)


def contact(request):
    title = 'контакты'
    heading = 'наши контакты'
    links_menu = get_links_menu(request, title=title, heading=heading)
    return render(request, 'geekshop/contact.html', context=links_menu)
