from .models import *
from django.forms import ModelForm, TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password','full_name']
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder':'Введите логин'}),
            "email": TextInput(attrs={'class': 'form-control', 'placeholder':'Введите почту'}),
            "password": TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder':'Введите пароль'}),
            "full_name": TextInput(attrs={'class': 'form-control', 'placeholder':'Введите Ф.И.О'}),
                   
                   }
   
  