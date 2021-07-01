from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='list'),
    path('read/<pk>/', ordersapp.OrderDetail.as_view(), name='detail'),
    path('create/', ordersapp.OrderCreate.as_view(), name='create'),
    path('update/<pk>/', ordersapp.OrderUpdate.as_view(), name='update'),
    path('delete/<pk>/', ordersapp.OrderDelete.as_view(), name='delete'),
    path('forming/complete/<pk>/', ordersapp.forming_complete, name='forming_complete'),
]
