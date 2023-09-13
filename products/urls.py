from django.urls import path
from . import views

urlpatterns = [
    path('products', views.product_list, name='products'),
    path('cart/<int:product_id>/', views.add_to_cart, name='cart'),
    path('single-product/<int:product_id>/', views.detail_product, name='single-product'),
    path('category/<int:category_id>/', views.product_by_category, name='product_by_category'),
    path('view_cart', views.view_cart, name='view_cart')
]