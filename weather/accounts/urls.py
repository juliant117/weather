from django.urls import path, include
from django.contrib.auth import urls as auth_urls
#from django.contrib.auth import views as auth_views
from. import views

app_name='accounts'

urlpatterns = [
    path("",views.login_view, name='login'),
    #path("",views.login_view,name="login"),
    #path('login/', views.login_view, name='login'),

]

