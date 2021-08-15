from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('surname', 'name', 'middle_name', 'username', 'password', 'email')


# Для ввода данных и создания новых объектов, можно воспользоваться формами - это шаблонизированная возможность
# ввода данных, которая связана с конкретной моделью

class LoginForm(ModelForm):
    class Meta:
        model = Student
        fields = ('username', 'password')
