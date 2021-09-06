from django.contrib import admin
from django.urls import path, include
from main.views import index, to_crm
from personalarea.views import lk
from CRM.views import StudentList, StudentDetail, UpdateProfileAdmin, show_students, Group_to_schedule, Update_group, \
    create_new_group, Group_list, Form_group
from personalarea.views import success_page

urlpatterns = [
    path('<int:pk>/', StudentDetail.as_view(), name='std_detail'),
    path('students/', StudentList.as_view(), name='std_list'),
    path('edit/<int:pk>', UpdateProfileAdmin.as_view(), name='edit_a'),
    path('edit/success', success_page, name='success'),
    path('group<int:group_name>/', show_students, name='group_list'),
    path('groups/', Group_to_schedule.as_view(), name='group_add'),
    path('update/<int:pk>', Update_group.as_view(), name='update_group'),
    path('create_group/', Group_list.as_view(), name='create_group'),
    path('add_group/', create_new_group, name='add_group'),
    path('form_group/', Form_group.as_view(),name='form_group')
]
