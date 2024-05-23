from django.db import models

class Program(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    iname = models.CharField(max_length=100)  # Assuming this is a typo and it should be 'name' instead of 'iname'
    fname = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.iname} {self.fname}"

