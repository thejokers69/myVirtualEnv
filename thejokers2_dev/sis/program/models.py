from django.db import models
from student.models import Student

class Program(models.Model):
    id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=100)
    prog_description = models.TextField()
    registration_fees = models.DecimalField(max_digits=10, decimal_places=2)

class RegistersFor(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
