from django.db import models
from django.utils import timezone


class User(models.Model):
  login = models.CharField(max_length=32)
  password = models.CharField(max_length=32)
  fname = models.CharField(max_length=32)
  mname = models.CharField(max_length=32)
  lname = models.CharField(max_length=32)
  info = models.TextField()
  created_date = models.DateTimeField(default=timezone.now) 
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.login