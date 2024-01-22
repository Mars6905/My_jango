from django.db import models


class Laptop(models.Model):

    title = models.CharField(max_length=80)
    memory = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Clothese(models.Model):

    size = models.CharField(max_length=80)
    color = models.CharField(max_length=80)
    style = models.CharField(max_length=80)
