from django.db import models

# Create your models here.
class News2015(models.Model):
    news_head = models.TextField(blank=True, null=True)
    news_date = models.DateField(blank=True, null=True)
    news_img = models.CharField(max_length=2048, blank=True, null=True)
    news_url = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_2015'