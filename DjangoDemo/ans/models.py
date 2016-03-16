from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
    addTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    personId = models.CharField(max_length=100)
    score = models.PositiveIntegerField()
    isDelete = models.BooleanField()