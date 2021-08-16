from django.contrib import admin
from django.contrib.auth.views import auth_logout
from django.urls import path, include
from main.views import index, to_crm, register, login, logout_from
from personalarea.views import lk

urlpatterns = [
    path('', index, name='mainpage'),
    path('lk/', lk, name='lk'),
    path('CRM/', to_crm, name='CRM'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', auth_logout, name='logout')
]
