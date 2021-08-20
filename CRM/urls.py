from django.contrib import admin
from django.urls import path, include
from main.views import index, to_crm
from personalarea.views import lk

from django.conf.urls import url
from CRM import views

urlpatterns = [
    path('<int:pk>/', views.StudentDetail.as_view(), name='CRM'),
    path('students/', views.StudentList.as_view(), name='std_list'),
]
