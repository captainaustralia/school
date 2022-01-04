from django.contrib.auth import authenticate, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth.views import auth_logout, PasswordResetView
from rest_framework.parsers import JSONParser
from main.forms import StudentRegistrationForm, ContactForm
from main.forms import Student, TypeSubscribe
from django.http import HttpResponse, JsonResponse

from main.models import Student_on_lesson
from main.serializers import Student_Serializer
from schedule.models import Days_Lesson
from main.models import Contacts

def to_crm(request):
    users = Student.objects.all()
    subs = TypeSubscribe.objects.all()
    day_info = Days_Lesson.objects.all()
    student_info = Student.objects.all()
    context = {'users': users, 'subs': subs, 'day': day_info, 'students': student_info}
    if request.user.is_superuser:
        return render(request, 'CRM/CRM.html', context)
    else:
        return render(request, 'index.html')


def register_page(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        if request.recaptcha_is_valid and user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return render(request, 'LK/lk.html', {'new_user': new_user})
    else:
        user_form = StudentRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def logout_from(request):
    auth_logout(request)
    return render(request, 'index.html')


def index(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            new_contact = contact.save(commit=False)
            new_contact.save()
            return render(request, 'index.html', {'new_contact': new_contact})
        else:
            pass
    else:
        contact = ContactForm()
    return render(request, 'index.html', {'contact': contact})


@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        attendance = Student_on_lesson.objects.all()
        serializer = Student_Serializer(attendance, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Student_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):
    try:
        attendance = Student_on_lesson.objects.get(pk=pk)
    except Student_on_lesson.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Student_Serializer(attendance)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Student_Serializer(attendance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        attendance.delete()
        return HttpResponse(status=204)
