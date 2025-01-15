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
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sequence_number = models.IntegerField(default=1)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            last_message = Message.objects.filter(chat=self.chat).order_by('sequence_number').last()
            if last_message:
                self.sequence_number = last_message.sequence_number + 1
            else:
                self.sequence_number = 1
        super(Message, self).save(*args, **kwargs)