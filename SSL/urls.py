
from django.urls import path
from . import views

urlpatterns = [
    path("<str:choice>/", views.index, name="choice"),
    path('', views.index, {'choice': 'home'}, name='home'),

    ]
