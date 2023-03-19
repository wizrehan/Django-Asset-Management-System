from django.urls import path

from . import views
  
urlpatterns = [

    path('view_stock/',views.ViewStock, name='view_stock'),
    path('search_stock/', views.SearchStock, name='search_stock'),
    path('print_stock_report/', views.PrintSearchedStock, name='printsearchedstock'),
    path('delete_stock/<id>', views.DeleteStock, name='delete_stock'),
    path('edit_stock/<id>', views.EditStock, name='editstock'),
    # path('update_stock/',views.UpdateStock, name='updated_stock'),
    
]