from django.db import models

# Create your models here.

#We need to define the page for the employee input

class EmployeeInput(models.Model):
    employee_name=models.CharField(max_length=20)
    employee_number= models.CharField(max_length=10)
    employee_email=models.CharField(max_length=30)

    class Meta:
        db_table="employeedetails"

    def __str__(self):
        return self.employee_number

    
