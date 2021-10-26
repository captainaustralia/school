from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from school.main.models import Student, TypeSubscribe, Student_Group
# from personalarea.views import UpdateProfile
# from schedule.models import Days_Lesson


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
    fields = ['last_name', 'first_name', 'age', 'email', 'balance', 'subs', 'payment', 'group_id']
    template_name = 'LK/edit_profile.html'
    success_url = 'success'


def show_students(request, group_name):
    students = Student.objects.all()
    users_in_group = students.filter(group_id=group_name)
    return render(request, 'CRM/choose_group.html', {'group': users_in_group})

#
# class Group_to_schedule(ListView):
#     model = Days_Lesson
#     context_object_name = 'Groups'
#     template_name = 'CRM/add_group.html'


class Group_list(ListView):
    model = Student_Group
    context_object_name = 'groups'
    template_name = 'CRM/create_group.html'

#
# class Update_group(UpdateView):
#     model = Days_Lesson
#     fields = ['day', 'time', 'group_id']
#     template_name = 'CRM/group_detail.html'


class Add_student_to_group(UpdateProfileAdmin):
    fields = ['last_name', 'group_id']


def create_new_group(request):
    if request.method == 'POST':
        name_group = request.POST['name_group']
        new_group = Student_Group(group_name=name_group)
        new_group.save()
        return render(request, 'CRM/CRM.html')

#
# class Form_group(CreateView):
#     model = Days_Lesson
#     fields = ['day', 'time', 'group_id']
#     template_name = 'CRM/form_group.html'
