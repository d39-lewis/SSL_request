
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.SSLView.as_view(),  name='user'),
    path('complete/', views.SSLView.as_view(),  name='complete'),
    ]
