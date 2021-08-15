from django.db import models


# Create your models here.
class Type_subscribe(models.Model):
    title = models.CharField(max_length=3)


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, blank=True, null=True)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.middle_name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=20, blank=False, null=False)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.middle_name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
