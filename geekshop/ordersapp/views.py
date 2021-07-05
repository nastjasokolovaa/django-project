from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from basketapp.models import Basket
from mainapp.context_processors import get_links, get_auth
from ordersapp.forms import OrderItemEditForm
from ordersapp.models import Order, OrderItem


class OrderList(ListView):
    model = Order

    def get_context_data(self, **kwargs):
        queryset = Order.objects.filter(user=self.request.user, is_active=True)

        context = {
            'object': queryset,
            'links': list(get_links()),
            'auth': list(get_auth(request=self.request)),
            'title': 'заказы',
        }
        return context


class OrderCreate(CreateView):
    model = Order
    success_url = reverse_lazy('ordersapp:list')
    fields = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemEditForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user=self.request.user)
            if len(basket_items):
                OrderFormSet = inlineformset_factory(
                    Order,
                    OrderItem,
                    form=OrderItemEditForm,
                    extra=len(basket_items)
                )
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
            else:
                formset = OrderFormSet()
        context = {
            'orderitems': formset,
            'links': list(get_links()),
            'auth': list(get_auth(request=self.request)),
            'title': 'создание заказы',
        }
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super().form_valid(form)


class OrderUpdate(UpdateView):
    model = Order
    success_url = reverse_lazy('ordersapp:list')
    fields = []
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemEditForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
        context = {
            'orderitems': formset,
            'links': list(get_links()),
            'auth': list(get_auth(request=self.request)),
            'title': 'редактирование заказа',
        }
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super().form_valid(form)


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('ordersapp:list')


class OrderDetail(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = list(get_links())
        context['auth'] = list(get_auth(request=self.request))
        context['title'] = 'подробнее'

        return context


def forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SEND_TO_PROCEED
    order.save()

    return HttpResponseRedirect(reverse('ordersapp:list'))
