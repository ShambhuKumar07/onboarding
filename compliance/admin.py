from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['uan_number', 'pan_number', 'esic_number']
    search_fields = ['uan_number', 'pan_number', 'esic_number']

admin.site.register(Employee, EmployeeAdmin)
