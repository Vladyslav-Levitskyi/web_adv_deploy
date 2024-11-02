from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('description', views.description, name='description'),
    path('git_projects', views.git_projects, name='git_projects'),
]

