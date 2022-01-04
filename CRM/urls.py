from django.contrib import admin
from django.urls import path, include
from main.views import index, to_crm
from personalarea.views import lk
from CRM.views import StudentList, StudentDetail, UpdateProfileAdmin, show_students, Create_group, Add_lesson, \
    add_payment, Payments_List, Groups_List, Group_Detail
from personalarea.views import success_page

urlpatterns = [
    path('<int:pk>/', StudentDetail.as_view(), name='std_detail'),
    path('students/', StudentList.as_view(), name='std_list'),
    path('edit/<int:pk>', UpdateProfileAdmin.as_view(), name='edit_a'),
    path('edit/success', success_page, name='success'),
    path('group<int:group_name>/', show_students, name='group_list'),
    path('create_group/', Create_group.as_view(), name='create_group'),
    path('add/', Add_lesson.as_view(), name='add_lesson'),
    path('add_payment/', add_payment, name='add_payment'),
    path('payment_list/', Payments_List.as_view(), name='payment_list'),
    path('group_list/', Groups_List.as_view(), name='gr_list'),
    path('groups_detail<int:pk>/', Group_Detail.as_view(), name='gr_detail'),

]
