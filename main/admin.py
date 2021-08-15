from django.contrib import admin

# Register your models here.
from main.models import Student, Type_subscribe, Teacher


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'middle_name', 'username', 'email', 'payment')
    list_display_links = ('surname', 'username')
    search_fields = ('surname', 'payment')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'payment')


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
