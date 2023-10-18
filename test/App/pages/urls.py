from django.urls import path ,include
from . import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('form',views.form2,name='form2'),
    path('form3',views.form3,name='form3'),
    path('end',views.f1,name="f1"),
    path('about',views.about,name="about")
]