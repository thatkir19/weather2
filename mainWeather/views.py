import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = 'decfdaed1323c30a8001086b9049f72a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(data=request.POST, files=request.FILES)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    city_info = ()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'wind': res["wind"]["speed"],
        }
        all_cities.append(city_info)

    context = {'info': city_info, 'form': form}

    return render(request, 'weather/mainpage.html', context)