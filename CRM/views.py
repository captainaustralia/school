from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from matplotlib import pyplot as plt

from CRM.forms import Payment_form
from CRM.models import Payments
from main.models import Student, TypeSubscribe, Student_Group
from personalarea.views import UpdateProfile
from schedule.models import Days_Lesson


class StudentList(ListView):
    model = Student
    context_object_name = 'StudentList'
    template_name = 'CRM/student_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            query_list = self.model.objects.filter(last_name=query)
        else:
            query_list = self.model.objects.all()
        return query_list


class StudentDetail(DetailView):
    model = Student
    context_object_name = 'students'
    template_name = 'CRM/student_detail.html'


class UpdateProfileAdmin(UpdateView):
    model = Student
    fields = ['last_name', 'first_name', 'age', 'email', 'balance', 'subs', 'payment']
    template_name = 'LK/edit_profile.html'
    success_url = 'success'


def show_students(request, group_name):
    all_groups = Days_Lesson.objects.all()
    users_in_group = all_groups.filter(group_id=group_name)
    return render(request, 'CRM/choose_group.html', {'students': users_in_group})


class Create_group(CreateView):
    model = Student_Group
    template_name = 'CRM/create_group.html'
    fields = ['group_name', 'students']


class Add_lesson(CreateView):
    model = Days_Lesson
    fields = ['day', 'time', 'group_id']
    template_name = 'CRM/add_to_schedule.html'


def add_payment(request):
    if request.method == 'POST':
        form = Payment_form(request.POST)
        pk = request.POST['student']
        a = Student.objects.get(pk=pk)
        a.balance += int(request.POST['pay'])
        a.save()
        form.save()
        return redirect('CRM')
    else:
        form = Payment_form()
    return render(request, 'CRM/add_payment.html', {'form': form})


class Payments_List(ListView):
    model = Payments
    context_object_name = 'pay_list'
    template_name = 'CRM/payments_list.html'


class Groups_List(ListView):
    model = Student_Group
    context_object_name = 'groups_list'
    template_name = 'CRM/groups_list.html'


class Group_Detail(UpdateView):
    model = Student_Group
    fields = ['students']
    template_name = 'CRM/groups_detail.html'


    # """ Отрисовка графика функции зависимости дохода от месяца"""
    # a = []
    # b = {}
    # summa = 0
    # all_obj = Payments.objects.all()
    # for j in range(1, 13):
    #     for i in all_obj:
    #         if i.date.month == j:
    #             summa += i.pay
    #     b[str(j)] = summa
    #     a.append(b)
    #     summa = 0
    #     b = {}
    #
    # x = []
    # y = []
    # for i in a:
    #     for k, v in i.items():
    #         x.append(k)
    #         y.append(v)
    # min_income = min(y)
    # max_income = max(y)
    # plt.plot(x,y)
    # plt.show()
