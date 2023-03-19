from django.urls import path

from . import views

urlpatterns = [

    path('view_designationa/',views.ViewDesignation, name='view_designation'),
    path('designation_delete/<user>/<id>', views.DeleteDesignation, name='deletedesignation'),
    path('designation_edit/<id>', views.EditDesignation, name='editdesignation'), 
    
]