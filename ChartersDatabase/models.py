from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


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
    contactEmail = models.EmailField(null=True, blank=True)
    contactPhone = models.CharField(max_length=16, null=True, blank=True)
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


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)

class Chat(models.Model):
    title = models.CharField(max_length=255)

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=255)
    