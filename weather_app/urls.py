from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterCreateView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('main-page/', views.MainPageView.as_view(), name = 'main-page')
]