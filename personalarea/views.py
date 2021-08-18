from django.shortcuts import render
from django.core.exceptions import BadRequest
# Create your views here.
from main.models import Student, TypeSubscribe


def lk(request):
    a = request.user.username
    users = Student.objects.all()
    subs = TypeSubscribe.objects.all()
    if request.user.is_authenticated:
        active = Student.objects.filter(username=a)
        active_1 = active.get()
        context = {'users': users, 'subs': subs, 'active': active_1}
        return render(request, 'lk.html', context)
    else:
        return render(request, 'index.html')
