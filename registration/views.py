from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
import requests
from user_profile.models import Profile


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "registration.html"

    def form_valid(self, form):
        form.save()

        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

