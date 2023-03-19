from django.urls import path

from . import views

urlpatterns = [

    path('add_stock/',views.add_stock, name='add_stock')
    
]