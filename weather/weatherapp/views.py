#weatherapp/views
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from . import openweather as ow
from django.conf import settings
from .models import citymodel as cm
from django.urls import reverse

import requests


def home(request): 
    try:
       
        user_preference = cm.objects.get()  
    except cm.DoesNotExist:
        user_preference = cm.objects.create()  

    if request.method == 'POST':
        new_city = request.POST.get('city')
        if new_city:
            user_preference.city = new_city
            user_preference.save()
           
            return redirect(f"{reverse('weatherapp:weather_view')}?city={new_city}")

    context = {'city': user_preference.city}  
    return render(request, 'weatherapp/home.html', context)


def weather_view(request):
    city = request.GET.get('city') or request.POST.get('city')
    if city:
        api_key= settings.OPENWEATHER_API_KEY
        forecast = ow.get_weather_forecast(city,api_key)

        if forecast:
            
            return render(request, 'weatherapp/forecast.html', {'forecast': forecast, 'city': city})
        else:
            return render(request, 'weatherapp/error.html', {'error_message': "Could not retrieve weather data."})
    else:
        return redirect('weatherapp:home')
    