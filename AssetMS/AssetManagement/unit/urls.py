from django.urls import path

from . import views

urlpatterns = [

    path('add_unit/',views.add_unit, name='add_unit'),
    
    
]