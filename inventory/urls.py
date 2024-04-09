from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_food, name='add_product'),
    path('', views.food_list, name='product_list'),
]