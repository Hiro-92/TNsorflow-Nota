from django.db import models

class Main(models.Model):
    location = models.FloatField(max_length=100)
    date = models.DateField(max_length=100)
    accident_type = models.CharField(max_length=20)
    dead = models.IntegerField(max_length=10)
    hurt = models.IntegerField(max_length=100)
