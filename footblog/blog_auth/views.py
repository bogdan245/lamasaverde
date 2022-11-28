from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate,get_user_model,login,logout

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, CreateView



class LoginRegistrationView(LoginView):
    login_form = LoginView
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


