from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    std_fname = models.CharField(max_length=255)
    std_lname = models.CharField(max_length=255)
    std_birth_date = models.DateField()
    std_email = models.EmailField()
    # Add a ManyToManyField for programs once the Program model is defined
