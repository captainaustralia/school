from django.contrib import admin
from django.urls import path, include
from main.views import index, to_crm
from personalarea.views import lk
from CRM.views import StudentList,StudentDetail
urlpatterns = [
    path('<int:pk>/', StudentDetail.as_view(), name='CRM'),
    path('students/', StudentList.as_view(), name='std_list'),
]
