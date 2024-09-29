import requests
from django.shortcuts import render

def weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')  
        api_key = '9835e52bf8f8c14ab8643d0f4a8f3be3' #API Key
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(api_url)
        weather_data = response.json()
        if weather_data.get('cod') == 200:
            context = {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed']
            }
        else:
            context = {'error': 'City not found!'}

        return render(request, 'weather/weather.html', context)
    
    return render(request, 'weather/weather.html')
