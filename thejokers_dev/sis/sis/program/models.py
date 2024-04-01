from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Program(models.Model):
    id = models.AutoField(primary_key=True)
    prog_name = models.CharField(max_length=255)
    prog_description = models.TextField()
    registration_fees = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    # Add a ManyToManyField for students once the Student model is defined

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    subject_description = models.TextField()
    class_field = models.CharField(max_length=255, blank=True)  # Adjust data type if needed for class representation

    def __str__(self):
        return self.subject_name
