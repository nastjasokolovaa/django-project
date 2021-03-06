from django.urls import path
from .views import products, product

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='products'),
    path('product/<int:pk>/', product, name='product'),
    path('category/<int:pk>/', products, name='category'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]
