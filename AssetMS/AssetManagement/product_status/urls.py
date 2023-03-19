from django.urls import path

from . import views

urlpatterns = [

    path('add_prodruct_status/',views.add_product_status, name='product_status')
    
] 