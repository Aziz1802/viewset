from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=('full_name',)

admin.site.register(Student,StudentAdmin)