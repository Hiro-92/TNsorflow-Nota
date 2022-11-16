from django.db import models

class About(models.Model):
    link = models.CharField(max_length=2048)