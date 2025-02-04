#weatherapp/urls
from django.urls import path, include
from django.contrib.auth import urls as auth_urls
#from django.contrib.auth import views as auth_views
from. import views

app_name='weatherapp'

urlpatterns = [
    path("",views.home, name='home'),
    path('weatherapp/',views.weather_view, name='weather_view')
]

