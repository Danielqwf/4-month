from django.shortcuts import render
from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import forms


class Registration(CreateView):
    form_class = forms.CustomRegistrationForm
    success_url = '/users/'
    template_name = 'custom_users/registration.html'


class EnterLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'custom_users/login.html'

    def get_success_url(self):
        return reverse('users:user_list')


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'custom_users/user_list.html'
