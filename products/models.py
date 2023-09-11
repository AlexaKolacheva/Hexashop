from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Корзина пользователя {self.user.username} ({self.quantity} товаров)'