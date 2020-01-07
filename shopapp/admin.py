from django.contrib import admin
from shopapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'father_name', 'roll',
                    's_name', 'address', 'email', 'password']
admin.site.register(Student,StudentAdmin)
