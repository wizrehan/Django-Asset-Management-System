from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models


class UserCreation(UserCreationForm):
     
    class Meta:
        model = User
        fields = [

            'username',
            
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            

        ]