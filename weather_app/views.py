from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import CustomRegisterForm

# Create your views here.
class RegisterCreateView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'weather_app/register.html'
    success_url = '/'