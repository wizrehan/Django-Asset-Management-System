from django.urls import path

from . import views

urlpatterns = [

    path('view_department/',views.ViewDepartment, name='view_department'),
    path('department_delete/<user>/<id>', views.DeleteDepartment, name='deletedepartment'),
    path('edit_department/<id>', views.EditDepartment, name='editdepartment'), 
    
]