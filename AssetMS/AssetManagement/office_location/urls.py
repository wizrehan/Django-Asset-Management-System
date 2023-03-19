from django.urls import path

from . import views

urlpatterns = [

    path('add_office/',views.add_office_loc, name='add_office')
    
]