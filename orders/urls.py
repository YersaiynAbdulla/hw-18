from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/edit/<int:customer_id>/', views.customer_edit, name='customer_edit'),
    path('customers/delete/<int:customer_id>/', views.customer_delete, name='customer_delete'),

    path('menu-items/', views.menu_item_list, name='menu_item_list'),
    path('menu-items/add/', views.menu_item_add, name='menu_item_add'),
    path('menu-items/edit/<int:item_id>/', views.menu_item_edit, name='menu_item_edit'),
    path('menu-items/delete/<int:item_id>/', views.menu_item_delete, name='menu_item_delete'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.order_add, name='order_add'),
    path('orders/edit/<int:order_id>/', views.order_edit, name='order_edit'),
    path('orders/delete/<int:order_id>/', views.order_delete, name='order_delete'),

    path('orders/items/<int:order_id>/', views.order_items_list, name='order_items_list'),
    path('orders/items/add/<int:order_id>/', views.order_item_add, name='order_item_add'),
    path('order-items/update/<int:order_item_id>/', views.order_item_update, name='order_item_update'),
]
