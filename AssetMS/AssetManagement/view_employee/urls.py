from django.urls import path

from . import views

urlpatterns = [

    path('view_employee/',views.ViewEmployee, name='view_employee'),
    path('employee_delete/<user>/<id>', views.DeleteEmployee, name='deleteEmployee'),
    path('employee_edit/<id>/<user>', views.EditEmployee, name='editemployee'), 
    path('employee_search/', views.SearchEmployee, name='searchemployee'), 
    path('print_employee_report/', views.PrintSearchedEmployee, name='printemployeereport'),

    
] 