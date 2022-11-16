from django.db import models

# Create your models here.
class AccidentGraph(models.Model):
    year = models.IntegerField(blank=True, null=True)
    pie = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accident_graph'



class AccidentLocal(models.Model):
    local = models.CharField(max_length=10, blank=True, null=True)
    bar = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accident_local'



