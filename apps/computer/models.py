from django.db import models


# Create your models here.

class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'
        verbose_name = 'Computer'
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ram = models.IntegerField()
    display_size = models.IntegerField()

    def __str__(self):
        return self.brand
