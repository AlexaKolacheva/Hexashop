from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('callback/', views.callbacks, name='callback'),
    path('reviews/', views.reviews, name='reviews'),
    path('comments/', views.add_comment, name='comments'),
    path('about/', views.about, name='about'),
    ]
=======
    path('', views.index, name='index'),
]
>>>>>>> 71f8e1e (authorization and html)
