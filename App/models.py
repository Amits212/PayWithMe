from django.db import models

class Parking(models.Model):
    region = models.CharField(max_length=50)
    duration = models.DurationField()

class Bus(models.Model):
    route = models.CharField(max_length=10)

class Bicycle(models.Model):
    region = models.CharField(max_length=50)
    duration = models.DurationField()

class Train(models.Model):
    route = models.CharField(max_length=10)

class TBpayment(models.Model):
    price = models.IntegerField()
    date = models.DateField()