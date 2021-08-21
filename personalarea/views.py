from django.shortcuts import render
from django.core.exceptions import BadRequest
# Create your views here.
from django.views.generic import UpdateView

from main.models import Student, TypeSubscribe


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
        context = {'users': users, 'subs': subs, 'active': active_1}
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
