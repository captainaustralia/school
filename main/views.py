from django.contrib.auth import authenticate, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import auth_logout, PasswordResetView

from main.forms import StudentRegistrationForm, ContactForm
from main.forms import Student, TypeSubscribe
from django.http import HttpResponse


def to_crm(request):
    users = Student.objects.all()
    subs = TypeSubscribe.objects.all()
    context = {'users': users, 'subs': subs}
    if request.user.is_superuser:
        return render(request, 'CRM/CRM.html', context)
    else:
        return render(request, 'intro.html')


def register_page(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        if request.recaptcha_is_valid and user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return render(request, 'intro.html', {'new_user': new_user})
    else:
        user_form = StudentRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def logout_from(request):
    # print('exit')
    auth_logout(request)
    return render(request, 'intro.html')


def index(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        new_contact = contact.save(commit=False)
        new_contact.save()
        return render(request, 'intro.html', {'new_contact': new_contact})
    else:
        contact = ContactForm()
    return render(request, 'intro.html', {'contact': contact})

