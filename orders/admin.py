from django.contrib import admin

# Register your models here.
from .models import Customer, MenuItem, Order, OrderItem

admin.site.register(Customer)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)