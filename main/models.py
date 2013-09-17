from django.db import models

# Create your models here.

class Brew(models.Model):
    #is used to tie a collection of temperature readings together and act as a log
    # to help note what beer is brewing and how it turns out
    beer_type = models.CharField(max_length=128)
    notes = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    target_temperature = models.FloatField()


class TemperatureData(models.Model):
    taken_at = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    target = models.FloatField()
    brew = models.ForeignKey(Brew)

