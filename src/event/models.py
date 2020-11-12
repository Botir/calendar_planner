from django.db import models

class Event(models.Model):

    title = models.CharField(max_length=255, null=False)
    start_date = models.DateField(null=False, )
    end_date = models.DateField(null=False, )
