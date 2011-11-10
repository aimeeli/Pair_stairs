from django.db import models

# Create your models here.

class Pair(models.Model):
    first_member = models.TextField()
    second_member = models.TextField()
    count = models.IntegerField()

class Programmer(models.Model):
    name = models.TextField()