from django.views.generic import TemplateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Customer, MenuItem, Order, OrderItem
from .forms import CustomerForm, MenuItemForm, OrderForm

# --- Customer Views ---
class CustomerListView(TemplateView):
    template_name = 'orders/customer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context

class CustomerCreateView(FormView):
    template_name = 'orders/customer_form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'orders/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'orders/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')

# --- MenuItem Views ---
class MenuItemListView(TemplateView):
    template_name = 'orders/menu_item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = MenuItem.objects.all()
        return context

class MenuItemCreateView(FormView):
    template_name = 'orders/menu_item_form.html'
    form_class = MenuItemForm
    success_url = reverse_lazy('menu_item_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'orders/menu_item_form.html'
    success_url = reverse_lazy('menu_item_list')

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'orders/menu_item_confirm_delete.html'
    success_url = reverse_lazy('menu_item_list')

# --- Order Views ---
class OrderListView(TemplateView):
    template_name = 'orders/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.kwargs.get('status')
        if status:
            context['orders'] = Order.objects.filter(status=status)
        else:
            context['orders'] = Order.objects.all()
        return context

class OrderCreateView(FormView):
    template_name = 'orders/order_form.html'
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')
