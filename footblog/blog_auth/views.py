from .form import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate,get_user_model,login,logout
from .form import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

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

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid:
        pass
    else:
        form = SignUpForm

    context = {"form":form}
    return render(request, "registration/login.html", context)

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