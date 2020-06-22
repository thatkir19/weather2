from django.contrib import admin
from .models import City
from registration.models import Profile


admin.site.register(Profile)
admin.site.register(City)

