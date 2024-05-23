from django.db import models

class Report(models.Model):
    date = models.DateField()
    num_trips = models.IntegerField()
    num_reservations = models.IntegerField()
    avg_rating = models.FloatField()

    def __str__(self):
        return f'Report for {self.date}'

