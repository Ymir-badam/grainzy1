from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    # path('cart/add1/', views.cart_add, name='cart_add'),
#     path('cart/item_clear/<str:id>/', views.item_clear, name='item_clear'),
#     path('cart/item_increment/<int:id>/',
#          views.item_increment, name='item_increment'),
#     path('cart/item_decrement/<int:id>/',
#          views.item_decrement, name='item_decrement'),
#     path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart-detail/',views.carts),
    path('cartitem-detail/',views.items1),
     path('add-to-cart/<str:product_name>/', views.add_to_cart, name='add_to_cart'),
     path('remove-to-cart/<str:product_name>/', views.remove_item, name='remove_to_cart'),
]
