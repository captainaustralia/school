from django.contrib import admin
from django.urls import path, include
from main.views import index, to_crm, Register_user, Login_user
from personalarea.views import lk

urlpatterns = [
    path('', index, name='mainpage'),
    path('lk/', lk, name='lk'),
    path('CRM/', to_crm, name='CRM'),
    path('register/', Register_user.as_view(), name='register'),
    path('login/', Login_user.as_view(), name='login')
]
