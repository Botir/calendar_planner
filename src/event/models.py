from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=255, null=False)
    start_date = models.DateField(null=False, )
    end_date = models.DateField(null=False, )


class Schedule(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    event_date = models.DateField(null=False)
