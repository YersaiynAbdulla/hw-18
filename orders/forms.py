from django import forms
from .models import Customer, MenuItem, Order, OrderItem

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category', 'available']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'items', 'status']

class OrderItemForm(forms.ModelForm): 
    class Meta:
        model = OrderItem
        fields = '__all__'