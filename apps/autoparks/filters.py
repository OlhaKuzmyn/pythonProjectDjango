import django_filters
from django_filters import rest_framework as filters

from apps.cars.models import CarModel

from .models import AutoParkModel

# class CustomField(filters.ModelMultipleChoiceFilter):
#     # def _check_values(self, value):
#     #     null = self.null_label is not None and value and self.null_value in value
#     #     if null:


class AutoParkFilter(filters.FilterSet):
    # cars_year_lt = filters.NumberFilter(field_name='cars__year', lookup_expr='lt')

    # cars_year_lt = filters.ModelMultipleChoiceFilter(field_name='cars__year', to_field_name='cars', lookup_expr='lt', queryset=AutoParkModel.objects.all())
    cars_year_lt = filters.ModelMultipleChoiceFilter(field_name='cars__year', to_field_name='year', lookup_expr='lt',
                                                     queryset=CarModel.objects.all())  # doesnt work

    # cars_year_lt = filters.AllValuesMultipleFilter(field_name='cars__year', lookup_expr='lt', qs=CarModel.objects.all())

    class Meta:
        model = AutoParkModel
        fields = ('cars',)
        # fields = ('name',)
