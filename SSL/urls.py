
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.SSLView, {'choice': 'home'}, name='home'),
    path('user/', views.SSLView, {'choice': 'user'}, name='user'),
    path('complete/', views.SSLView, {'choice': 'complete'}, name='complete'),
    ]
