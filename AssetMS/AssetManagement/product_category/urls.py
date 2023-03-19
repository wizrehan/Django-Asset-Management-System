from django.urls import path

from . import views

urlpatterns = [

    path('add_prod_cat/',views.add_product_category, name='product_category')
    
]