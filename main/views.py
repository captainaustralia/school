import json

from django.contrib.auth import authenticate, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import auth_logout, PasswordResetView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .forms import StudentRegistrationForm, ContactForm
from .forms import Student, TypeSubscribe
from django.http import HttpResponse


# from .models import Days_Lesson


# def to_crm(request):
#     users = Student.objects.all()
#     subs = TypeSubscribe.objects.all()
#     day_info = Days_Lesson.objects.all()
#     student_info = Student.objects.all()
#     context = {'users': users, 'subs': subs, 'day': day_info, 'students': student_info}
#     if request.user.is_superuser:
#         return render(request, 'CRM/CRM.html', context)
#     else:
#         return render(request, 'intro.html')


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
        # data = json.loads(request.body)
        contact = ContactForm(request.POST)
        # contact.phone = data['phone']
        # contact.name = data['name']
        new_contact = contact.save(commit=False)
        new_contact.save()
        response = {'message': 'Contacted successfully'}
        return Response(response, status=status.HTTP_200_OK)
    else:
        contact = ContactForm()
        response = {'message': 'Please enter stars for the rating'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
