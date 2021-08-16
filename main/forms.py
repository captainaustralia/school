from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Student
from django.contrib.auth.models import User  # Импортируем класс, чтобы унаследоваться от него
from django.forms import CharField, IntegerField, PasswordInput


class UserRegistrationForm(ModelForm):  # Создаем форму, в которой опишем класс и его атрибуты
    password_1 = CharField(max_length=20, min_length=6, widget=PasswordInput)  # Создаем поле ввода пароля
    password_2 = CharField(max_length=20, min_length=6, widget=PasswordInput)  # Повторное поле пароля
    age = IntegerField()  # Добавляем поле ввода возраста

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'age')

    def check_pass(self):
        data = self.cleaned_data
        if data['password_1'] != data['password_2']:
            raise ValidationError('Неверный повтор пароля')
        return data['password_1']


class StudentRegistrationForm(ModelForm):
    password_1 = CharField(max_length=20, min_length=6, widget=PasswordInput)  # Создаем поле ввода пароля
    password_2 = CharField(max_length=20, min_length=6, widget=PasswordInput)  # Повторное поле пароля

    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', 'email', 'age')

    def check_pass(self):
        data = self.cleaned_data
        if data['password_1'] != data['password_2']:
            raise ValidationError('Неверный повтор пароля')
        return data['password_1']


# class StudentForm(ModelForm):
#     all_username = Student.objects.all()
#
#     class Meta:
#         model = Student
#         fields = ('surname', 'name', 'middle_name', 'username', 'password', 'email')
#
# # Для ввода данных и создания новых объектов, можно воспользоваться формами - это шаблонизированная возможность
# # ввода данных, которая связана с конкретной моделью
#
# class LoginForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ('username', 'password')
