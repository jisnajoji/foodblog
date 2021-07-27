from django.urls import path
from . import views

urlpatterns=[
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('dec/<int:product_id>/',views.min_cart,name='deccart'),
    path('remove/<int:product_id>/',views.cart_delete,name='removecart'),

  
]