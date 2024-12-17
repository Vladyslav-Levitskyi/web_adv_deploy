from django.shortcuts import render, redirect
from .forms import PersonForm
from dotenv import load_dotenv
from django.http import JsonResponse
from weather.openweathermap import get_weather
from django.views.decorators.csrf import ensure_csrf_cookie
import os
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def home(request):
    try:
        return render(request, 'core_app/home.html')
    except Exception as e:
        logger.error(f"Error rendering home page: {str(e)}")
        return render(request, 'core_app/error.html', {'error': str(e)})

def description(request):
    return render(request, 'core_app/description.html')

def git_projects(request):
    return render(request, 'core_app/git_projects.html')

def add_user(request):
    error = ''
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Form is invalid. Please try again."

    form = PersonForm()
    form_methods = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/profile.html', form_methods)


    
    
    