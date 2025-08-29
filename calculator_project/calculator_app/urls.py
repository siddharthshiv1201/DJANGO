# calculator_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL for a welcome message/instructions
    path('', views.calculate_home),
    path('calculate/', views.calculate_home, name='calculate_home'),

    # URL for operations requiring two values (e.g., add, power)
    path('calculate/<str:operation>/<str:value1>/<str:value2>/', views.calculate, name='calculate_two_values'),
    
    # URL for operations requiring one value (e.g., sqrt, sin)
    path('calculate/<str:operation>/<str:value1>/', views.calculate, name='calculate_one_value'),
]