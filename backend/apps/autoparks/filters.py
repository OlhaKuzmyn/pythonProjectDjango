from django_filters import rest_framework as filters

from .models import AutoParkModel


class AutoParkFilter(filters.FilterSet):
    cars_year_lt = filters.NumberFilter(field_name='cars', lookup_expr='year__lt')

    class Meta:
        model = AutoParkModel
        fields = ('cars_year_lt',)
