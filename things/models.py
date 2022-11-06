from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

class thing(models.Model):
    #random test
    name = models.CharField(max_length = 30, unique = True, blank = False)
    description = models.CharField(max_length = 120)
    quantity = models.IntegerField(validators = [MaxValueValidator(100), MinValueValidator(0)])
