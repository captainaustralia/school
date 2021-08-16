from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
# from main.models import Student

from main.forms import UserRegistrationForm, StudentRegistrationForm, LoginForm


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


def login(request):
    if request.user.is_active:
        print('Авторизован')
    else:
        print('не авторизован')
    login_form = LoginForm(request.POST)
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            print('Авторизован')
            if user is not None:
                if not user.is_active:
                    authenticate(request, user)
                    return HttpResponse('Поздравляем, вы вошли!')
                else:
                    return logout_from(request)
            else:
                return HttpResponse('Логина не существует')
        login_form = LoginForm()
    return render(request, 'lk.html', {'login_form': login_form})


def logout_from(request):
    print('Вышел')
    logout(request)
    return render(request, 'index.html')
