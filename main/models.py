from django.db import models
from django.contrib.auth.models import User


class Student(User):
    age = models.IntegerField(null=False)
    payment = models.BooleanField(default=False)
    subs = models.ForeignKey('TypeSubscribe', on_delete=models.PROTECT, null=True)
    balance = models.IntegerField(null=True)

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


class Contacts (models.Model):
    phone = models.IntegerField()
    name = models.CharField(max_length=20)
