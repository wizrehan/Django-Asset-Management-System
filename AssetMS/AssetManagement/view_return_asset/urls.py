from django.urls import path

from . import views

urlpatterns = [

    path('view_return_asset/',views.ViewReturnAsset, name='viewreturnasset'),
    
] 