from django.urls import path

from . import views

urlpatterns = [

    path('view_product_status/',views.ViewProductStatus, name='view_product_status'),
    path('delete_product_status/<user>/<id>',views.DeleteProductStatus, name='deleteproductstatus'),
    path('edit_product_status/<id>/<user>', views.EditProductStatus, name='edit_product_status'),
    
]