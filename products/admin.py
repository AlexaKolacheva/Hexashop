from django.contrib import admin
from .models import Category, Product, Cart, CartItem, PurchaseHistory,Order


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(PurchaseHistory)
admin.site.register(Order)


# Register your models here.
