from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyRegisterFormView.as_view(), name="reg"),
]