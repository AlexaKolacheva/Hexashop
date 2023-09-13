from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem, Category
from django.core.paginator import Paginator


def product_by_category(request, category_id):
    # Получите выбранную категорию
    category = Category.objects.get(pk=category_id)

    # Фильтруйте продукты по выбранной категории
    products = Product.objects.filter(category=category)
    items_per_page = 3
    paginator = Paginator(products, items_per_page)

    # Получите номер текущей страницы из параметра запроса (GET)
    page_number = request.GET.get('page')

    # Получите объект страницы продуктов
    page = paginator.get_page(page_number)

    context = {'products': products, 'category': category}
    return render(request, 'main/products.html', context)


def product_list(request):
    # Получите список всех продуктов из базы данных
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'main/products.html', context)


def detail_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'main/single-product.html', context)



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Проверяем, есть ли пользователь, иначе используем анонимного пользователя
    user = request.user

    # Получаем корзину пользователя (или создаем новую, если нет)
    cart, created = Cart.objects.get_or_create(user=user)

    # Пытаемся найти продукт в корзине

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


def view_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item = CartItem.objects.filter(cart=cart)
    return render(request, 'main/cart.html', {'cart_item': cart_item, 'cart': cart})

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Проверяем, есть ли пользователь, иначе используем анонимного пользователя
    user = request.user

    # Получаем корзину пользователя (или создаем новую, если нет)
    cart, created = Cart.objects.get_or_create(user=user)

    # Попробуйте найти продукт в корзине и удалить его
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass  # Если товар не найден в корзине, ничего не делаем

    return redirect('view_cart')







def increase_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

def decrease_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item = CartItem.objects.get(cart=cart, product=product)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        pass
    return redirect('view_cart')



