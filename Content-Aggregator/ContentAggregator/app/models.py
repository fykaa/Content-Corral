# Create your models here.
from django.db import models
 
# Create your models here.
class PyContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.headline
 
class ProgContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.headline
 
class HiringContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.headline
 
class CovidContent(models.Model):
  headline = models.CharField(max_length=300)
  img = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.headline