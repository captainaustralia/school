# from django.db import models
# from main.models import Student, Teacher
#
#
# class Lesson(models.Model):
#     time = models.DateTimeField
#     students = models.OneToOneField(Student, on_delete=models.PROTECT)  # One to many?
#     teachers = models.OneToOneField(Teacher, on_delete=models.PROTECT)  # also?
#     students_active = models.QuerySet(Student)
#
#
# class Schedule_Day(models.Model):
#     date = models.DateTimeField()
#     days = models.IntegerField(default=7)
#     lessons = models.OneToOneField(Lesson, on_delete=models.PROTECT)  # One to many?
#
#
# class Schedule_Month(models.Model):
#     month_name = models.CharField()
#     month_num = models.IntegerField(default=12)
#     current_month = models.IntegerField(default=1)
#