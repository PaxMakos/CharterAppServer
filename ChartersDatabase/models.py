from django.db import models
from django.contrib.auth.models import User


class Port(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.URLField()
    places = models.IntegerField()
    description = models.TextField()


class Boat(models.Model):
    name = models.CharField(max_length=100)
    boatModel = models.CharField(max_length=100)
    productionYear = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    draft = models.IntegerField()
    company = models.CharField(max_length=100)
    motherPort = models.ForeignKey(Port, on_delete=models.PROTECT)
    beds = models.IntegerField()
    pricePerDay = models.IntegerField()
    description = models.TextField()


class Charter(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
