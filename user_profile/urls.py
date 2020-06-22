from django.urls import path
from .views import user_profile, logout


urlpatterns = [
    path('', user_profile, name="user_profile"),
    path('/login', logout, name="logout"),
]