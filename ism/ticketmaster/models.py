from django.db import models

class User(models.Model):
  user_name = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  def __str__(self):
    return self.user_name

class Seat(models.Model):
  position = models.CharField(max_length=60)
  def __str__(self):
    return str(self.position)

class Segment(models.Model):
  segmentId = models.CharField(max_length=60)
  placesTotal = models.IntegerField()
  placesAvailable = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=1)
 
  def __str__(self):
    return str(self.segmentId)
# Create your models here.
