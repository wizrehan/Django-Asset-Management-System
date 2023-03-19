from django.urls import path

from . import views

urlpatterns = [

    path('view_product/',views.ViewProduct, name='view_product'),
    path('product_delete/<user>/<id>', views.DeleteProduct, name='deleteproduct'),
    path('edit_product/<id>/<user>', views.EditProduct, name='editproduct'),
    path('search_product/', views.SearchProduct, name='searchproduct'),
    path('print_product/',  views.PrintSearchedProduct, name='printsearchedproduct'),
    
] 