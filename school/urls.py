from django.contrib import admin
from django.urls import path, include

import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='mainpage'),
    path('lk/', include('personalarea.urls'), name='lk'),
    path('CRM/', include('CRM.urls'), name='CRM'),
    # path('add/', main.views.take_contact, name='add')
    # path('schedule/', include('schedule.urls'), name='schedule')

]
