from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import path, include, reverse_lazy

import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('lk/', include('personalarea.urls'), name='lk'),
    path('CRM/', include('CRM.urls'), name='CRM'),
    path('reset/', PasswordResetView.as_view(template_name='registration/pass_reset.html',
                                             success_url=reverse_lazy('password_reset_done')), name='reset'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(template_name='registration/pass_reset_done.html'), name='password_reset_done'),
    path('password_complete/',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete')

]
