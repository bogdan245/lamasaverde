from django.contrib import admin
from django.urls import path
# from .views import UserRegister
from .views import LoginRegistrationView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('member/', LoginRegistrationView.as_view(), name='login'),
    path('member/', LoginRegistrationView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')

]
