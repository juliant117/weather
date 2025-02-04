#weatherapp/views
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from . import openweather as ow
from django.conf import settings
from .models import citymodel as cm
from django.urls import reverse

import requests


def weather_view(request):
    city = request.POST.get('city') or request.GET.get('city') or 'Bogota'
    forecast = None
    error_message = None

    if city:
        api_key = settings.OPENWEATHER_API_KEY
        forecast = ow.get_weather_forecast(city, api_key)

        # Translate conditions
        if forecast:
            for day in forecast:
                day['conditions'] 
        else:
            error_message = "No se pudo obtener el pronóstico del clima."

    return render(request, 'weatherapp/unique.html', {
        'city': city,
        'forecast': forecast,
        'error_message': error_message
    })

