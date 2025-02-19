from django import template
from orders.models import MenuItem

register = template.Library()

@register.filter
def filter_orders_by_status(orders, status):
    return orders.filter(status=status)

@register.filter
def filter_menu_by_category(menu_items, category):
    return menu_items.filter(category=category)
