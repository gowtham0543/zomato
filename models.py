from django.db import models

# Create your models here.
class item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()

class feedback(models.Model):
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
