# student/models.py
from django.db import models
from program.models import Program  # Import the Program model from the program app

class Student(models.Model):
    std_fname = models.CharField(max_length=50)
    std_lname = models.CharField(max_length=50)
    std_birth_date = models.DateField()
    std_email = models.EmailField()
    prog = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.std_fname} {self.std_lname}'
