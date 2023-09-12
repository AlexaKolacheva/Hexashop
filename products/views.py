from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart


def product_list(request):
    # Получите список всех продуктов из базы данных
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'main/products.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Предполагается, что у вас есть способ получить текущего пользователя
    user = request.user

    # Создайте корзину для пользователя, если ее еще нет
    cart, created = Cart.objects.get_or_create(user=user)

    # Попробуйте найти продукт в корзине
    cart_item, item_created = cart.products.get_or_create(product=product)

    if not item_created:
        # Если продукт уже есть в корзине, увеличьте его количество на 1
        cart_item.quantity += 1
        cart_item.save()

    return redirect('main/cart.html')

