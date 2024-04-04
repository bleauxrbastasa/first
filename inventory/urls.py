from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('dashboard/', views.home, name="dashboard"),
    path('inventory/', views.inventory, name='inventory'),
    path('customer/', views.customer, name='customer'),
    path('create_item/', views.createItem, name='create_item'),
    path('update_item/<str:pk>/', views.updateItem, name='update_item'),
    path('delete_item/<str:pk>/', views.deleteItem, name='delete_item'),
    path('expiry/', views.expiry_view, name='expiry'),
]

