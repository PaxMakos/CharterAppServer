from django.db import models
from django.contrib.auth.models import User


class Port(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    places = models.IntegerField(null=True, blank=True)
    description = models.TextField(default="")
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)


class Boat(models.Model):
    name = models.CharField(max_length=100)
    boatModel = models.CharField(max_length=100)
    productionYear = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField(null=True, blank=True)
    draft = models.IntegerField()
    company = models.CharField(max_length=100)
    motherPort = models.ForeignKey(Port, on_delete=models.PROTECT, null=True, blank=True)
    beds = models.IntegerField()
    pricePerDay = models.IntegerField()
    description = models.TextField()


class Charter(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
