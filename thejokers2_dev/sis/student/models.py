from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    std_fname = models.CharField(max_length=50)
    std_lname = models.CharField(max_length=50)
    std_birth_date = models.DateField()
    std_email = models.CharField(max_length=100)
    prog_id = models.IntegerField()
