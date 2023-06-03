from rest_framework import serializers

from backend.models import Employee

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["emp_id","name","email","contact"]