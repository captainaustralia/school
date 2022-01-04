import calendar

from django.db import models
from main.models import Student, Student_Group


class Days_Lesson(models.Model):
    """ Base model for create lesson """
    time_choices = [
        ('8:30', '8:30'),
        ('10:00', '10:00'),
        ('11:30', '11:30'),
        ('13:00', '13:00'),
        ('14:30', '14:30'),
        ('16:00', '16:00'),
        ('17:30', '17:30')
    ]
    day_choices = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    ]
    day = models.CharField(
        max_length=15,
        choices=day_choices,
        default='1'
    )
    time = models.CharField(
        max_length=6,
        choices=time_choices,
        default='1'
    )
    group_id = models.ForeignKey(
        Student_Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('CRM')

    def __str__(self):
        return self.day + ' ' + self.time
