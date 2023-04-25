from django.contrib import admin

# Register your models here.
from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','phone','address')
    search_fields = ['name']
    list_filter = ['address']

admin.site.register(Student, StudentAdmin)