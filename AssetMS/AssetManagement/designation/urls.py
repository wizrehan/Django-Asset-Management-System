from django.urls import path

from . import views

urlpatterns = [

    path('add_designation/',views.add_designation, name='add_designation')
    
]