from django.core.validators import RegexValidator
from django.db import models

from .enums import RegEx


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_park'
        ordering = ['id']

    name = models.CharField(max_length=50, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
