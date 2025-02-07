from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterCreateView.as_view(), name='register')
]