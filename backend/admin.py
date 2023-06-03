from django.contrib import admin
from django.contrib.admin import register
from backend.models import Employee
# Register your models here.
@register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields=["emp_id"]
    list_display = ["emp_id", "name", "email", "contact"]

