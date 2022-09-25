from django.db import models
from django.db.models.base import Model

# Create your models here.

class Upcoming_event(models.Model) :
    event_object = models.BooleanField(help_text="Please keep it checked if there is any upcoming event and uncheck it after completion of the event.")
    name = models.CharField(max_length=100)
    image = models.TextField(help_text="Upload the image to Cloudinary website and generate a link and paste it here.")
    reglink = models.TextField()
    description = models.TextField()
    teamsize = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    medium = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100, help_text="Name1 mentioned in Poster")
    name2 = models.CharField(max_length=100, help_text="Name2 mentioned in Poster")
    contact1 = models.CharField(max_length=100, help_text="Please maintain the formate - +91 00000 00000")
    contact2 = models.CharField(max_length=100, help_text="Please maintain the formate - +91 00000 00000")

    def __str__(self):
        return self.name

class Event(models.Model) :
    event_id = models.TextField(max_length=100, help_text="Event id should be unique. use the following formate - eventnameyear for example parichaya2021. Please note no space should be given in between.")
    name = models.CharField(max_length=100)
    image = models.TextField(help_text="Upload the image to Cloudinary website and generate a link and paste it here.")
    summary = models.TextField()
    teamsize = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    medium = models.CharField(max_length=100)
    winner_object = models.BooleanField(help_text="Please keep it checked if there is any winner. if there are no winners keep it unchecked and write any random values in winner and runner fields")
    winner = models.TextField(help_text="Please mention name, year and branch. If there are multiple people use <br> tag to separate each winner.")
    runner = models.TextField(help_text="Please mention name, year and branch. If there are multiple people use <br> tag to separate each runner.")
    participants =models.IntegerField()

    def __str__(self):
        return self.name

