from django.urls import path

from . import views

urlpatterns = [

    path('view_office_location/',views.ViewOfficeLocation, name='view_office_location'),
    path('office_loc_delete/<user>/<id>', views.DeleteOfficeLocation, name='deleteofficeloc'),
    path('edit_office_loc/<id>/<user>', views.EditOfficeLocation, name='editofficeloc'), 
    
]