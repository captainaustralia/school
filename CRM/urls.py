from django.contrib import admin
from django.urls import path, include
from main.views import index, to_crm
from personalarea.views import lk
from CRM.views import StudentList, StudentDetail, UpdateProfileAdmin
from personalarea.views import success_page

urlpatterns = [
    path('<int:pk>/', StudentDetail.as_view(), name='std_detail'),
    path('students/', StudentList.as_view(), name='std_list'),
    path('edit/<int:pk>', UpdateProfileAdmin.as_view(), name='edit_a'),
    path('edit/success', success_page, name='success')
]
