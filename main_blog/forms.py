from .models import *
from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError
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
        
     
    def clean(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError("Эта почта уже зарегестрированна")
        return data
        
        
   
  