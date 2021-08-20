from django.contrib import admin
from django.urls import path, include
from main.views import index, to_crm
from personalarea.views import lk, UpdateProfile, success_page

urlpatterns = [
    path('edit/<int:pk>', UpdateProfile.as_view(), name='edit'),
    path('edit/success', success_page, name='success')
]
