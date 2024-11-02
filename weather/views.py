from django.shortcuts import render, redirect
from .forms import CityForm
from .openweathermap import get_weather
from dotenv import load_dotenv
import requests
import os
import datetime

load_dotenv()


def weather_view(request):
    city = request.session.get('city_name')
    weather_data = None

    if city:
        api_key = os.getenv('OPENWEATHER_KEY')
        weather_data = get_weather(city, api_key)
        if weather_data:
            sunrise_time = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
            sunset_time = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
            weather_data['sys']['sunrise_time'] = sunrise_time
            weather_data['sys']['sunset_time'] = sunset_time

    context = {
        'weather_icon': weather_data['weather'][0]['icon'] if weather_data else None,
        'temperature': weather_data['main']['temp'] if weather_data else None,
        'city_name': city,
        'weather_data': weather_data,
    }
    return render(request, 'weather/weather.html', context)


def set_city(request):   
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            request.session['city_name'] = city
            return redirect('weather')
        return redirect('weather')
