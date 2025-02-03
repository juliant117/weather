from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from . import openweather as ow
from django.conf import settings

import requests
# Create your views here.
def weather_view(request):
    
    city = "Bogota"
    api_key= settings.OPENWEATHER_API_KEY
    forecast = ow.get_weather_forecast(city,api_key)

    if forecast:
        return render(request, 'weatherapp/home.html', {'forecast': forecast, 'city': city})
    else:
        return render(request, 'weatherapp/error.html', {'error_message': "Could not retrieve weather data."})
    