from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView
from main.models import Student, TypeSubscribe
from personalarea.views import UpdateProfile


class StudentList(ListView):
    model = Student
    context_object_name = 'StudentList'
    template_name = 'CRM/student_list.html'


class StudentDetail(DetailView):
    model = Student
    context_object_name = 'students'
    template_name = 'CRM/student_detail.html'


class UpdateProfileAdmin(UpdateView):
    model = Student
    fields = ['last_name', 'first_name', 'age', 'email', 'balance','subs', 'payment']
    template_name = 'LK/edit_profile.html'
    success_url = 'success'
