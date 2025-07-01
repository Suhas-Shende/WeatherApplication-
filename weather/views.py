from django.shortcuts import render,HttpResponse
import json
import requests



def weather(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=fe271c5829dec9ab020b4eee19f8cba3'
            response = requests.get(api_url.format(city))
            result = response.json()

            if result.get("cod") == 200:
                data = {
                    "city": city.title(),
                    "country_code": result['sys']['country'],
                    "coordinate": f"{result['coord']['lon']}°, {result['coord']['lat']}°",
                    "temp": round(result['main']['temp'] - 273.15, 2),  # Kelvin to Celsius
                    "humidity": result['main']['humidity'],
                    "description": result['weather'][0]['description'].capitalize(),
                    "icon": result['weather'][0]['icon'],  # optional: for displaying weather icon
                }
            else:
                data["error"] = f"City '{city}' not found. Please try again."
        else:
            data["error"] = "Please enter a city name."
    
    return render(request, 'weather.html', {'data': data})








