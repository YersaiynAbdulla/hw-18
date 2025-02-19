from django.urls import path
from .views import (
    CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    MenuItemListView, MenuItemCreateView, MenuItemUpdateView, MenuItemDeleteView,
    OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    OrderItemsListView, OrderItemCreateView, OrderItemUpdateView
)

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/edit/<int:pk>/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),

    path('menu-items/', MenuItemListView.as_view(), name='menu_item_list'),
    path('menu-items/add/', MenuItemCreateView.as_view(), name='menu_item_add'),
    path('menu-items/edit/<int:pk>/', MenuItemUpdateView.as_view(), name='menu_item_edit'),
    path('menu-items/delete/<int:pk>/', MenuItemDeleteView.as_view(), name='menu_item_delete'),
    
    # Фильтрация блюд по категории
    path('menu-items/category/<str:category>/', MenuItemListView.as_view(), name='menu_item_by_category'),

    # Фильтрация заказов по статусу
    path('orders/status/<str:status>/', OrderListView.as_view(), name='order_list_by_status'),

    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/add/', OrderCreateView.as_view(), name='order_add'),
    path('orders/edit/<int:pk>/', OrderUpdateView.as_view(), name='order_edit'),
    path('orders/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),

    path('orders/items/<int:order_id>/', OrderItemsListView.as_view(), name='order_items_list'),
    path('orders/items/add/<int:order_id>/', OrderItemCreateView.as_view(), name='order_item_add'),
    path('order-items/update/<int:pk>/', OrderItemUpdateView.as_view(), name='order_item_update'),
]
