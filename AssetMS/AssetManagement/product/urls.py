from django.urls import path

from . import views

urlpatterns = [

    path('create_product/',views.add_product, name='add_product')
    
]