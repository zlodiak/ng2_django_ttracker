from django.db import models
from django.utils import timezone
from app_users.models import User


class Status(models.Model):
  title = models.CharField(max_length=32)
  created_date = models.DateTimeField(default=timezone.now) 
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title 


class Task(models.Model):
  user = models.ForeignKey(User)
  status = models.ForeignKey(Status, default=1)
  title = models.CharField(max_length=32)
  body = models.TextField()
  deadline_date = models.DateTimeField(default=timezone.now, blank=False, null=False) 
  created_date = models.DateTimeField(default=timezone.now) 
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title


   