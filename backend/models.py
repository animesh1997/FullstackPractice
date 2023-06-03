from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    emp_id = models.IntegerField(auto_created=True)
    contact = models.IntegerField()
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return str(self.emp_id)
