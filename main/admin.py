from django.contrib import admin
from main.forms import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'age', 'email', 'payment')
    list_display_links = ('first_name', 'last_name', 'username', 'age', 'email', 'payment')
    search_fields = ('surname', 'payment')


admin.site.register(Student, StudentAdmin)
