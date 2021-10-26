# from django.conf.urls import url
# from django.contrib import admin
# from django.contrib.auth.views import auth_logout, LoginView, PasswordResetView, PasswordResetDoneView, \
#     PasswordResetConfirmView
from django.urls import path, include, reverse_lazy

# from .decorators import check_recaptcha
from .views import index, register, logout_from
# from .views import lk


urlpatterns = [
    path('contact/', index),

    # path('lk/', lk, name='lk'),
    # path('CRM/', to_crm, name='CRM'),
    # path('register/', check_recaptcha(register), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', logout_from, name='logout'),
]
