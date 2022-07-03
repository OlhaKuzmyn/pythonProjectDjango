from django.db import models


class AuthoParkModel(models.Model):
    class Meta:
        db_table = 'autho_park'

    name = models.CharField(max_length=50)
