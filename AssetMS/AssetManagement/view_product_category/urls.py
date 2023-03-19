from django.urls import path

from . import views

urlpatterns = [

    path('view_product_category/',views.ViewProductCategory, name='view_product_category'),
    path('delete_product_category/<user>/<id>', views.DeleteProductCategory, name= 'deleteproductcategory'),
    path('edit_product_category/<id>/<user>', views.EditProductCategory, name='edit_product_cat'),

    
]