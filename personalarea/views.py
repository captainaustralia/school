import qrcode
from django.shortcuts import render
from django.core.exceptions import BadRequest
# Create your views here.
from django.views.generic import UpdateView

from CRM.models import Payments
from main.models import Student, TypeSubscribe
import os

from schedule.models import Days_Lesson


def lk(request):
    a = request.user.username
    users = Student.objects.all()
    subs = TypeSubscribe.objects.all()
    if request.user.is_superuser:
        return render(request, 'index.html')
    elif request.user.is_authenticated:
        active = Student.objects.filter(username=a)
        active_1 = active.get()
        active_1.update_balance()
        day_info = Days_Lesson.objects.all()
        student_info = Student.objects.all()
        payments = Payments.objects.filter(student=active_1.id)
        context = {'users': users, 'subs': subs, 'active': active_1, 'day': day_info, 'student': student_info,
                   'payments': payments}
        string = active_1.username
        file = active_1.username + '.jpg'
        image = qrcode.make(string)
        stud_id = active_1.id
        if str(active_1.id) + '.png' not in '/static/img/QR':
            image.save(f'static/img/QR/{stud_id}.png')
        return render(request, 'LK/lk.html', context)
    else:
        return render(request, 'index.html')


class UpdateProfile(UpdateView):
    model = Student
    fields = ['last_name', 'first_name', 'age', 'email']
    template_name = 'LK/edit_profile.html'
    success_url = 'success'


def success_page(request):
    return render(request, 'LK/update_done.html')
