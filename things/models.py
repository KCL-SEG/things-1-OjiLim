from django.db import models
from django.db.models.Model

class Thing(models.Model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()


# Create your models here.
