from django.contrib import admin
from main.forms import Student, TypeSubscribe


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'age', 'email', 'payment', 'subs','balance')
    list_display_links = ('first_name', 'last_name', 'username', 'age', 'email', 'payment')
    search_fields = ('surname', 'payment')


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('types',)


admin.site.register(TypeSubscribe)
admin.site.register(Student, StudentAdmin)
