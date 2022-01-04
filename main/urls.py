from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import auth_logout, LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView
from django.urls import path, include, reverse_lazy

from main.decorators import check_recaptcha
from main.views import index, to_crm, register, logout_from, student_list, student_detail
from personalarea.views import lk

urlpatterns = [
    path('', index, name='mainpage'),
    path('lk/', lk, name='lk'),
    path('CRM/', to_crm, name='CRM'),
    path('register/', check_recaptcha(register), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_from, name='logout'),
    path('attendance/', student_list),
    path('attendance/<int:pk>', student_detail)
]
