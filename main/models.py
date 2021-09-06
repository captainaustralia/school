import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField


class Student_Group(models.Model):
    group_name = models.CharField(max_length=20)

    def __str__(self):
        return self.group_name


class Student(User):
    age = models.IntegerField(null=False)
    payment = models.BooleanField(default=False)
    subs = models.ForeignKey('TypeSubscribe', on_delete=models.CASCADE, null=True)
    balance = models.IntegerField(default=0, blank=True)
    group_id = models.ForeignKey(Student_Group, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.username + self.last_name

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
