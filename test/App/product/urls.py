from django.urls import path ,include
from . import views 

urlpatterns=[
    path('',views.product,name='product'),
     path('all',views.products,name='products')
]