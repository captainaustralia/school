from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.models import Student
from main.forms import StudentForm, LoginForm


def index(request):
    return render(request, 'index.html')


def to_crm(request):
    return render(request, 'CRM.html')


def register_page(request):
    return render(request, 'register.html')


class Register_user(CreateView):
    template_name = 'register.html'
    form_class = StudentForm
    success_url = reverse_lazy('mainpage')


class Login_user(CreateView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('mainpage')
