from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weather_view, name='weather'),
    path('set_city/', views.set_city, name='set_city'),
]