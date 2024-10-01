from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    age = forms.CharField(max_length=10, default = '0')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'password1', 'password2']
    

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.Charfield(max_length= 10)
    password = forms.CharField(label = 'password', widget=forms.PasswordInput)

#done with forms for authentication