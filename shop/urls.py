from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('bedroom',views.bedroom,name='bedroom'),
    path('livingroom',views.livingroom,name='livingroom'),
    path('diningroom',views.diningroom,name='diningroom'),
    path('bedding',views.bedding,name='bedding'),
    path('youth',views.youth,name='youth'),
    path('newarrival',views.newarrival,name='newarrival'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout, name='logout'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('product/<int:id>',views.product,name='product'),
    path('cart_detail',views.cart_detail,name='cart_detail'),
    path('cart_add/<int:id>',views.cart_add,name='cart_add'),
    path('cart_remove/<int:id>',views.cart_remove,name='cart_remove'),
    path('checkout',views.checkout,name='checkout'),
    path('order',views.order, name='order'),
    path('orderview/<str:t_no>',views.orderview, name='orderview'),
    path('payment_process',views.payment_process, name='payment_process'),
    path('payment_done', views.payment_done, name='payment_done'),
    path('payment_cancelled',views.payment_cancelled, name= 'payment_cancelled'),
]