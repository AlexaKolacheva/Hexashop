from django.urls import path
from . import views

urlpatterns = [

    path('callback/', views.callbacks, name='callback'),
    path('reviews/', views.reviews, name='reviews'),
    path('comments/', views.add_comment, name='comments'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]

