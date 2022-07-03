from rest_framework.serializers import ModelSerializer

from .models import AuthoParkModel
from apps.cars.serializers import CarSerializer


class AuthoParkSerializer(ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AuthoParkModel
        fields = ('id', 'name', 'cars')
