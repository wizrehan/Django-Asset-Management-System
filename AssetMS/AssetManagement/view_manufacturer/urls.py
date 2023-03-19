from django.urls import path

from . import views

urlpatterns = [

    path('view_manufacturer/',views.ViewManufacturer, name='view_manufacturer'),
    path('manufacturer_delete/<user>/<id>', views.DeleteManufacturer, name='deletemanufacturer'),
    path('edit_manufacturer/<id>/<user>', views.EditManufacturer, name='editmanufacturer'),
    
]