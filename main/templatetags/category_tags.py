from django import template
from products.models import Category  # Замените 'your_app' на имя вашего приложения и импортируйте модель категории

register = template.Library()


@register.inclusion_tag('categories_menu.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
