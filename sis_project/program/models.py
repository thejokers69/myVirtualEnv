# program/models.py
from django.db import models

class Program(models.Model):
    prog_name = models.CharField(max_length=100)
    prog_description = models.TextField()
    registration_fees = models.DecimalField(max_digits=8, decimal_places=2)
    subjects = models.ManyToManyField('Subject', through='ProgramSubject')

    def __str__(self):
        return f'{self.prog_name}'

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_description = models.TextField()
    class_hours = models.IntegerField()

    def __str__(self):
        return f'{self.subject_name}'

class ProgramSubject(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # You can add additional fields specific to the Program-Subject relationship here, if needed

    def __str__(self):
        return f'{self.program} : {self.subject}'
