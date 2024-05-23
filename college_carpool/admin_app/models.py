from django.db import models

class Report(models.Model):
    report_date = models.DateField(auto_now_add=True)
    total_trips = models.IntegerField()
    total_users = models.IntegerField()

    def __str__(self):
        return f"Report {self.report_date}"


class Comment:
    pass