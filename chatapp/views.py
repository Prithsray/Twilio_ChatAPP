from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        # Handle user registration form submission
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('chat_rooms')
    return render(request, 'registration/register.html')

def user_login(request):
    if request.method == "POST":
        # Handle user login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat_rooms')
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


# chatapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .twilio_service import send_sms

def registration_view(request):
    # Your registration code here
    # After successful registration, send an SMS
    send_sms(to='+916294785483', body='Welcome to our chat app!')

    return render(request, 'registration.html')
