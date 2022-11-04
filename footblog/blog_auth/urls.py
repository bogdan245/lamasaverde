from django.contrib import admin
from django.urls import path
# from .views import UserRegister
from .views import signUp



urlpatterns = [
    path('signup/', signUp.as_view(), name='signup')

]
