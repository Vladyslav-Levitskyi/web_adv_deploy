from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('register/', views.register, name="register"),
    path('accounts/profile/', views.profile, name="profile"),
    path('', RedirectView.as_view(url='/', permanent=True)),
]

