from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import path, include, reverse_lazy

import main.views
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('lk/', include('personalarea.urls'), name='lk'),
    path('CRM/', include('CRM.urls'), name='CRM'),
    path('schedule/', include('schedule.urls')),
    path('reset/', PasswordResetView.as_view(template_name='registration/pass_reset.html',
                                             success_url=reverse_lazy('password_reset_done')), name='reset'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(template_name='registration/pass_reset_done.html'), name='password_reset_done'),
    path('password_complete/',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
