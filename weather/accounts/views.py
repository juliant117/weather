from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.method == "POST":
        print(f"Current URL: {request.path}")  # Print the current URL
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('weatherapp:weather')  

    else:

        form=AuthenticationForm()

    return render(request, 'accounts/login.html',{'form':form})


    