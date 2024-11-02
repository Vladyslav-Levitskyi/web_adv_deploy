from weather.openweathermap import get_weather
from dotenv import load_dotenv
import os

load_dotenv()

def weather_processor(request):
    api_key = os.getenv("OPENWEATHER_KEY")
    city = request.session.get('city_name')
    weather_data = None  # Ініціалізуємо weather_data тут
    show_form = False

    if not city:
        show_form = True
        print('city is None')
    else:
        weather_data = get_weather(city, api_key)
    
    if weather_data:
        return {
            'weather_icon': weather_data['weather'][0]['icon'],
            'temperature': weather_data['main']['temp'],
            'city_name': weather_data['name'],
            'weather_data': weather_data,
            'show_form': False
        }
    else:
        return {
            'weather_icon': None,
            'temperature': None,
            'city_name': None,
            'weather_data': None,
            'show_form': show_form
        }