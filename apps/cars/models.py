from django.db import models

from apps.autho_parks.models import AuthoParkModel

class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    autho_park = models.ForeignKey(AuthoParkModel, on_delete=models.CASCADE, related_name='cars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
