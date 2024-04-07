from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.customer_home, name='customer_home'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('view-products/', views.view_products, name='view_products'),
    path('login/', views.customer_login, name='customer_login'),
    path('signup/', views.customer_signup, name='customer_signup'),
    path('about/', views.customer_about, name='about'),
    path('orders/', views.orders, name='orders'),
    path('payment-options/', views.payment_options, name='payment_options'),
    path('delivery-settings/', views.delivery_settings, name='delivery_settings'),
    
    
    path('messages/', views.support_messages, name='support_messages'),
    path('messages/send/', views.send_message, name='send_message'),
    
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delivery-settings/', views.delivery_settings, name='delivery_settings'),
    path('set-delivery-options/', views.set_delivery_options, name='set_delivery_options'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('cart/', views.cart_view, name='cart'),  # Adding the URL pattern for the cart
    path('view_users/', views.view_users, name='view_users'),
]
