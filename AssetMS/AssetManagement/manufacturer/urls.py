from django.urls import path

from . import views

urlpatterns = [

    path('add_manufac/',views.add_manufacturer, name='manufacturer')
    
]