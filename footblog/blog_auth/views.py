from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import forms
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import signUpForm


# class UserRegister(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('home')


class signUp(generic.CreateView):
    form_class = signUpForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')




