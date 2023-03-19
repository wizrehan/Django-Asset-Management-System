from django.urls import path

from . import views

urlpatterns = [

    path('return_asset/',views.Return_Asset, name='returnasset'),
    
] 