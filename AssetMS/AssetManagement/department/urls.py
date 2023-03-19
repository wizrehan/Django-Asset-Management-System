from django.urls import path

from . import views

urlpatterns = [

    path('add_department/',views.add_department, name='add_department')
    
]