from django.contrib import admin
from main.forms import Student, TypeSubscribe, Contacts
from main.models import Student_Group, Student_on_lesson
from schedule.models import Days_Lesson


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email', 'payment')
    list_display_links = ('last_name',)
    search_fields = ('last_name',)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('types',)


admin.site.register(TypeSubscribe)
admin.site.register(Student, StudentAdmin)
admin.site.register(Contacts)
admin.site.register(Student_Group)
admin.site.register(Days_Lesson)
admin.site.register(Student_on_lesson)
