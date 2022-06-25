from django.db import models


# Create your models here.

class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ram = models.IntegerField()
    display_size = models.IntegerField()
