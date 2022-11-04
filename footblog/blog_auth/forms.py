from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signUpForm(UserCreationForm):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']