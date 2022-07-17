from django_filters import rest_framework as filters

from .models import AutoParkModel


class AutoParkFilter(filters.FilterSet):
    # cars_year_lt = filters.NumberFilter(field_name='cars__year__lt')
    cars_year_lt = filters.ModelMultipleChoiceFilter(field_name='cars__year', to_field_name='cars', lookup_expr='lt', queryset=AutoParkModel.objects.all())

    class Meta:
        model = AutoParkModel
        fields = ('cars',)
        # fields = ('name',)
