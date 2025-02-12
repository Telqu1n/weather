from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CustomRegisterForm, CustomLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
class RegisterCreateView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'weather_app/register.html'
    success_url = 'main-page'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return response


class LoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'weather_app/login.html'
    next_page = reverse_lazy('main-page')    
   

class MainPageView(TemplateView):
    template_name = 'weather_app/main_page.html'