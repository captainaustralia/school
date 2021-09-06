from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Student, TypeSubscribe, Contacts
from django.contrib.auth.models import User
from django.forms import CharField, IntegerField, PasswordInput, TextInput, NumberInput, Textarea


class StudentRegistrationForm(ModelForm):
    password_1 = CharField(max_length=20, min_length=6, widget=PasswordInput)
    password_2 = CharField(max_length=20, min_length=6, widget=PasswordInput)

    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', 'email', 'age')

    def check_pass(self):
        data = self.cleaned_data
        if data['password_1'] != data['password_2']:
            raise ValidationError('Неверный повтор пароля')
        return data['password_1']


class Subscribe(ModelForm):
    class Meta:
        model = TypeSubscribe
        fields = ('types',)


class ContactForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ('phone', 'name')
