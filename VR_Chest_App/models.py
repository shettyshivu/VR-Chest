from django.db import models

# Create your models here.
class Feedback(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Messege = models.TextField()

class Appointment(models.Model):
    Name = models.CharField(max_length=50)
    Mobileno=models.BigIntegerField()
    Email = models.CharField(max_length=50)
    Date = models.DateField()
    Time=models.TimeField()
    Doctor=models.CharField(max_length=30)
    