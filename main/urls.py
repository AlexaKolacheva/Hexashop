from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('callback/', views.callbacks, name='callback'),
    ]
=======
    path('', views.index, name='index'),
]
>>>>>>> 71f8e1e (authorization and html)
