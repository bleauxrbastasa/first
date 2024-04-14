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
    path('add-scheduled-delivery/', views.add_scheduled_delivery, name='add_scheduled_delivery'),
    path('delivery-list/', views.delivery_list, name='delivery_list'),
    path('update-delivery-status/', views.update_delivery_status, name='update_delivery_status'),
    path('add_order/', views.add_order, name='add_order'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
      path('new_order/', views.new_order, name='new_order'),
]

