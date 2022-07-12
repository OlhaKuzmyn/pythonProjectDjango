from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from apps.autoparks.models import AutoParkModel

from .enums import RegEx


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=100, validators=[RegexValidator(RegEx.BRAND.pattern, RegEx.BRAND.msg)])
    price = models.IntegerField(validators=[RegexValidator(RegEx.PRICE.pattern, RegEx.PRICE.msg)])
    year = models.IntegerField(
        validators=[MaxValueValidator(date.today().year),
                    MinValueValidator(date.today().year - 20)],
        error_messages={'incorrect value': 'car should be be of a current year or maximum 20 years old'}  # doesnt work
    )
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
