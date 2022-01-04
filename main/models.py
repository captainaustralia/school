import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField
from django.urls import reverse_lazy


class Student(User):
    age = models.PositiveIntegerField(null=True)
    payment = models.BooleanField(default=False)
    subs = models.ForeignKey('TypeSubscribe', on_delete=models.SET_NULL, null=True)
    balance = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.last_name

    def update_balance(self):
        if self.balance > 0:
            self.payment = True
            self.save()
        else:
            self.payment = False
            self.save()

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class Student_Group(models.Model):
    group_name = models.CharField(max_length=50, blank=False)
    students = models.ManyToManyField(Student, related_name="students")

    def __str__(self):
        return self.group_name

    def get_absolute_url(self):
        return reverse_lazy('CRM')


class TypeSubscribe(models.Model):
    types = models.CharField(max_length=30)

    def __str__(self):
        return self.types

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Contacts(models.Model):
    phone = models.IntegerField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + ' ' + str(self.phone)


class Student_on_lesson(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return str(self.date) + ' ' + str(self.student.name)
