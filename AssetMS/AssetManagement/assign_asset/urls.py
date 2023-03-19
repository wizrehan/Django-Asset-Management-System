from django.urls import path

from . import views

urlpatterns = [

    path('assign_asset/',views.assign_asset, name='assign_asset'),
    path('search_asset', views.SearchAsset, name='searchasset'), 
    path('print_asset/', views.PrintSearchedAsset, name= 'printsearchedasset'),
]