from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate,get_user_model,login,logout
from .form import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, CreateView

# class UserRegister(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('home')


# class signUp(generic.CreateView):
#     form_class = signUpForm
#     template_name = 'registration/login.html'
#     success_url = reverse_lazy('home')


class LoginRegistrationView(LoginView, SignUpForm):
    login_form = LoginView
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    # def login(self, request):
    #     if 'signin' in request.POST:
    #         form_class = self.login_form(request.POST)
    #         form = self.get_form_class()
    def get_success_url(self):
        return reverse_lazy('home')

# class signup(generic.CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('home')
#     template_name = 'registration/signup.html'
#
#     def post(self, request, *args, **kwargs):
#         if 'signup' in request.POST:
#             form_class = self.get_form_class()
#             form = self.get_form(form_class)
#             if form.is_valid():
#                 form.save()
#             return self.form_valid(form)






    # def signUp(request):
    #     signup_form = SignUpForm
    #     if signup_form.is_valid:
    #         pass
    #     else:
    #         signup_form = SignUpForm()
    #     return render(request, "signup")



# class RegisterPage(FormView):
#     template_name = 'registration/login.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('home')

