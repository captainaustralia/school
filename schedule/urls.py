from django.urls import path

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import auth_logout, LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView
from django.urls import path, include, reverse_lazy

import schedule.views
from main.decorators import check_recaptcha
from main.views import index, to_crm, register, logout_from
from personalarea.views import lk

urlpatterns = [
    path('', schedule.views.schedule, name='schedule')
]
