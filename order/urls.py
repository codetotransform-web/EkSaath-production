from django.urls import path
from . import views



urlpatterns = [
    path('cart/<int:id>', views.cart_view,name='cart'),
    path('set_cart/', views.set_cart_view,name='set_cart'),
    path('del_cart/',views.del_cart_view,name='del_cart'),
    path('unconfirmed_order/<int:customer_id>',views.unconfirmed_order_view,name="unconfirmed_order"),
    path('address_for_order/<int:customer_id>',views.address_for_order_view,name='address_for_order'),
    path('edit_delivery_address/<int:customer_id>',views.edit_delivery_address,name='edit_delivery_address'),
    path('order/<int:customer_id>',views.order_view,name="order"),
]
