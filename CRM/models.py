from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy

from main.models import Student


# Create your models here.


class Payments(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    pay = models.PositiveIntegerField(blank=False, null=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    payment_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse_lazy('CRM')
