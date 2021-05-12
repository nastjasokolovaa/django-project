from django.urls import path
from .views import basket, basket_add, basket_remove

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='basket'),
    path('add/<int:pk>', basket_add, name='basket_add'),
    path('add/<int:pk>', basket_remove, name='basket_remove'),
]
