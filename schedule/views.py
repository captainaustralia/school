from django.shortcuts import render
from django.views.generic import ListView

from main.models import Student
from schedule.models import Days_Lesson, Student_Group


# Create your views here.

def schedule(request):
    day_info = Days_Lesson.objects.all()
    student_info = Student.objects.all()
    context = {'day': day_info, 'student': student_info}
    return render(request, 'schedule.html', context)


def index_1(request):
    return render(request, 'intro.html')
