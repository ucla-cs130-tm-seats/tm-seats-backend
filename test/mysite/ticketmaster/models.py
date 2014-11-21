from django.db import models

class User(models.Model):
  user_name = models.CharField(max_length=200)
  password = models.CharField(max_length=200)
  def __str__(self):
    return self.user_name

class Seat(models.Model):
  number = models.IntegerField(default=0)
  user = models.ForeignKey(User)
  def __str__(self):
    return str(self.number)
# Create your models here.
