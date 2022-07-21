from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from .enums import RegEx

UserModel = get_user_model()

class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_park'
        ordering = ['id']

    name = models.CharField(max_length=50, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    owners = models.ManyToManyField(UserModel, related_name='auto_park')
