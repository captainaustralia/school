from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='mainpage'),
    path('lk/', include('personalarea.urls'), name='lk'),
    path('CRM/', include('CRM.urls'), name='CRM')
]
