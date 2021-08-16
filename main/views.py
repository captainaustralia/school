from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
# from main.models import Student

from main.forms import UserRegistrationForm,StudentRegistrationForm


def index(request):
    return render(request, 'index.html')


def to_crm(request):
    return render(request, 'CRM.html')


def register_page(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return render(request, 'lk.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


# class Register_user(CreateView):
#     template_name = 'register.html'
#     form_class = StudentForm
#     success_url = reverse_lazy('mainpage')
#
#
# class Login_user(CreateView):
#     template_name = 'login.html'
#     form_class = LoginForm
#     success_url = reverse_lazy('mainpage')
