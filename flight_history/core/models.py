from django.db import models


class Flight(models.Model):
    icao = models.CharField(max_length=50)
    number = models.IntegerField()
    di = models.CharField(max_length=1)
    line = models.CharField(max_length=1)
    departure_date = models.CharField(max_length=20, blank=True, null=True)
    departure_date_real = models.CharField(
        max_length=20, blank=True, null=True)
    arrival_date = models.CharField(max_length=20, blank=True, null=True)
    arrival_date_real = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1)
    arrival = models.CharField(max_length=10)
    departure = models.CharField(max_length=10)
    code = models.CharField(max_length=2, blank=True, null=True)
