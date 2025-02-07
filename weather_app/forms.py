from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }