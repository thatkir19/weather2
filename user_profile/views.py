from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import requests
from .models import Profile
from .forms import ProfileCityForm


def user_profile(request):
    appid = 'decfdaed1323c30a8001086b9049f72a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = ProfileCityForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        form.save()

    form = ProfileCityForm()
    if User.is_active:
        cities = Profile.objects.filter(user=request.user)
    else:
        cities = Profile.objects.all()
    city_info = ()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.user_city)).json()
        city_info = {
            'city': city.user_city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'wind': res["wind"]["speed"],
        }
        all_cities.append(city_info)

    context = {'info': city_info, 'form': form}

    return render(request, 'user_profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

