from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,get_user_model,login,logout
from .form import *
from django.contrib.auth.views import LoginView, LogoutView

# class UserRegister(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('home')


# class signUp(generic.CreateView):
#     form_class = signUpForm
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('home')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = ['username', 'password']
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

