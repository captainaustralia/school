from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView
from main.models import Student, TypeSubscribe


class StudentList(ListView):
    model = Student
    context_object_name = 'StudentList'
    template_name = 'CRM/student_list.html'


class StudentDetail(DetailView):
    model = Student
    context_object_name = 'students'
    template_name = 'CRM/student_detail.html'

