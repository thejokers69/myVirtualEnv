# subject/models.py

from django.db import models

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    subject_description = models.TextField()
    class_hours = models.IntegerField()
