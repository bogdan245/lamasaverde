from django.contrib import admin
from django.urls import path
# from .views import UserRegister
from .views import CustomLoginView



urlpatterns = [
    path('member/', CustomLoginView.as_view(), name='login')

]
