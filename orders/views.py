from django.views.generic import TemplateView, FormView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Customer, MenuItem, Order, OrderItem
from .forms import CustomerForm, MenuItemForm, OrderForm, OrderItemForm

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
from django.views.generic import ListView
from .models import MenuItem

class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'menu/menu_item_list.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.kwargs.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


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
from django.views.generic import ListView
from .models import Order

class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.kwargs.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


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

# --- Order Item Views ---
class OrderItemsListView(TemplateView):
    template_name = 'orders/order_items_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = get_object_or_404(Order, id=self.kwargs['order_id'])
        context['order'] = order
        context['items'] = OrderItem.objects.filter(order=order)
        return context

class OrderItemCreateView(FormView):
    template_name = 'orders/order_item_form.html'
    form_class = OrderItemForm

    def form_valid(self, form):
        order = get_object_or_404(Order, id=self.kwargs['order_id'])
        order_item = form.save(commit=False)
        order_item.order = order
        order_item.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('order_items_list', kwargs={'order_id': self.kwargs['order_id']})

class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'orders/order_item_form.html'

    def get_success_url(self):
        return reverse_lazy('order_items_list', kwargs={'order_id': self.object.order.id})
