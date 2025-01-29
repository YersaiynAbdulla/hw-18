from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, MenuItem, Order, OrderItem
from .forms import CustomerForm, MenuItemForm, OrderForm

# Create your views here.
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'orders/customer_list.html', {'customers': customers})

def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'orders/customer_form.html', {'form': form})

def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'orders/customer_form.html', {'form': form})

def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'orders/customer_confirm_delete.html', {'customer': customer})

def menu_item_list(request):
    items = MenuItem.objects.all()
    return render(request, 'orders/menu_item_list.html', {'items': items})

def menu_item_add(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_item_list')
    else:
        form = MenuItemForm()
    return render(request, 'orders/menu_item_form.html', {'form': form})

def menu_item_edit(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu_item_list')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'orders/menu_item_form.html', {'form': form})

def menu_item_delete(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('menu_item_list')
    return render(request, 'orders/menu_item_confirm_delete.html', {'item': item})

def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def order_items_list(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = order.orderitem_set.all()
    return render(request, 'orders/order_items_list.html', {'order': order, 'items': items})

def order_item_add(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        menu_item_id = request.POST.get('menu_item')
        quantity = int(request.POST.get('quantity', 1))
        menu_item = get_object_or_404(MenuItem, id=menu_item_id)
        OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
        order.total_price_calculator()
        return redirect('order_items_list', order_id=order.id)
    menu_items = MenuItem.objects.filter(available=True)
    return render(request, 'orders/order_item_form.html', {'order': order, 'menu_items': menu_items})

def order_item_update(request, order_item_id):
    order_item = get_object_or_404(OrderItem, id=order_item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        order_item.quantity = quantity
        order_item.save()
        order_item.order.total_price_calculator()
        return redirect('order_items_list', order_item.order.id)
    return render(request, 'orders/order_item_form.html', {'order_item': order_item})
