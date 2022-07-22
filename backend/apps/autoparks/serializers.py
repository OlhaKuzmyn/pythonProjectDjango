from rest_framework.serializers import ModelSerializer

from apps.cars.serializers import CarSerializer
from apps.users.serializers import UserSerializer

from .models import AutoParkModel


class AutoParkSerializer(ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    owners = UserSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars', 'owners')
        read_only_fields = ('owners',)
