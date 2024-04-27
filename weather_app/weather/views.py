from django.shortcuts import render

# weather_app/views.py
from django.shortcuts import render
from .utils import get_weather

def weather(request):
    city = request.GET.get('city', 'London')
    api_key = '9db75a91f86d54c0317c20f430ded473'  # Replace with your API key
    weather_data = get_weather(api_key, city)
    context = {'weather_data': weather_data}
    return render(request, 'weather.html', context)

