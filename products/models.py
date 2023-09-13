from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media', blank=True)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    @property
    def total_price(self):
        return sum(i.final_price for i in self.cart_items.all())

    @property
    def final_quantity(self):
        return sum(i.quantity for i in self.cart_items.all())

    def __str__(self):
        return f'Cart for {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def final_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.quantity} x {self.product_name}'

