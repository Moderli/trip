from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the desired URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the desired URL after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

import requests
from django.shortcuts import render

import random

def generate_daily_tour_plans():
    tour_plans = [
        "Visit a local museum and explore the exhibits.",
        "Take a scenic hike in a nearby nature reserve.",
        "Enjoy a guided city tour to learn about local history and culture.",
        "Have a picnic in a beautiful park with a view.",
        "Try local cuisine at a highly recommended restaurant.",
        "Take a boat tour to explore nearby islands or waterways.",
        "Visit a historical landmark and learn about its significance.",
        "Attend a live music or cultural performance in the evening.",
        "Relax at a spa and indulge in some pampering.",
        "Join a group activity such as a cooking class or art workshop.",
        
    ]

    # Shuffle the plans and select 5 for a day
    random.shuffle(tour_plans)
    daily_plans = random.sample(tour_plans, 5)

    return daily_plans

from django.contrib.auth.decorators import login_required

def place_details(request):
    if request.method == 'POST':
        place_name = request.POST.get('place_name')

        # Fetch Wikipedia extract for the specified place
        wikipedia_api_url = f'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&titles={place_name}'

        try:
            response = requests.get(wikipedia_api_url)
            data = response.json()
            pages = data.get('query', {}).get('pages', {})
            page_id = next(iter(pages))
            extract = pages[page_id].get('extract', '')
        except Exception as e:
            extract = None

        # Generate 5 random plans for the day
        daily_tour_plans = generate_daily_tour_plans()

        return render(request, 'home.html', {'extract': extract, 'daily_tour_plans': daily_tour_plans})

    return render(request, 'home.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    # Redirect to the desired URL after logout
    return redirect('login')


