from django.contrib.auth import authenticate, logout
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import auth_logout
from main.forms import StudentRegistrationForm
from main.forms import Student, TypeSubscribe
from django.http import HttpResponse


def index(request):
    return render(request, 'intro.html')


def to_crm(request):
    users = Student.objects.all()
    subs = TypeSubscribe.objects.all()
    context = {'users': users, 'subs': subs}
    if request.user.is_superuser:
        return render(request, 'CRM/CRM.html', context)
    else:
        return render(request, 'index.html')


def register_page(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password_1'])
            new_user.save()
            return render(request, 'LK/lk.html', {'new_user': new_user})
    else:
        user_form = StudentRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def logout_from(request):
    # print('exit')
    auth_logout(request)
    return render(request, 'index.html')
