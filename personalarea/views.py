from django.shortcuts import render
from django.core.exceptions import BadRequest
# Create your views here.
from main.models import Student, TypeSubscribe


def lk(request):
    users = Student.objects.all()
    subs = TypeSubscribe.objects.all()
    context = {'users': users, 'subs': subs}
    if request.user.is_authenticated:
        return render(request, 'lk.html', context)
    else:
        return render(request,'index.html')