from django.db import models

class news(models.Model):
    news_head = models.CharField(max_length=200)
    news_agency = models.CharField(max_length=100)
    news_date = models.CharField(max_length=200)
    news_img = models.CharField(max_length=200)
    news_link = models.CharField(max_length=200)