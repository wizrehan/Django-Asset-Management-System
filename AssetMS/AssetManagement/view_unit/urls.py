from django.urls import path

from . import views

urlpatterns = [

    path('view_unit/',views.ViewUnit, name='view_unit'),
    # path('view_crud/', views.ViewCRUD, name='crud' ), 
    path('unit_delete/<user>/<id>', views.DeleteUnitCopy, name='deleteunit'),
    path('edit_unit/<id>', views.EditUnit, name='editunit'), 
     
]  