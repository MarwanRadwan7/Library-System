from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'user')
    search_fields = ('id',)

admin.site.register(Student, StudentAdmin)
