import requests
import os

def get_weather(city, api_key):
    if not api_key:
        raise ValueError("API key is missing")
    base_url = "http://api.openweathermap.org./data/2.5/weather?"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    if city is None:
        url = None
    else:    
        url = base_url + 'appid=' + api_key + '&q=' + city
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None