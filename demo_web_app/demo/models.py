from django.db import models

class DataPoint(models.Model):
    date = models.DateField()
    value = models.IntegerField()
    
    class Meta():
        ordering = ('date', )