from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainWeather.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^user_profile/', include('user_profile.urls')),
]
