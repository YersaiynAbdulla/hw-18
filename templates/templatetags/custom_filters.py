from django import template
from orders.models import MenuItem

register = template.Library()

@register.filter
def filter_orders_by_status(orders, status):
    """Фильтрует заказы по переданному статусу."""
    return orders.filter(status=status)

@register.filter
def filter_menu_by_category(menu_items, category):
    """Фильтрует меню по переданной категории."""
    return menu_items.filter(category=category)
