from django.urls import path
from . import views

urlpatterns = [

    path('products', views.product_list, name='products'),
    path('cart/<int:product_id>/', views.add_to_cart, name='cart')

]