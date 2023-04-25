from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'phone', 'address', 'age', 'gender')
    # search_fields = ['name']
    # list_filter = ['luong']


admin.site.register(Teacher, TeacherAdmin)
from django.contrib import admin

# Register your models here.
