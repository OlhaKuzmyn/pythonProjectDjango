from rest_framework.serializers import ModelSerializer

from apps.computer.models import ComputerModel


class ComputerSerializer(ModelSerializer):
    class Meta:
        model = ComputerModel
        fields = ('id', 'brand', 'model', 'ram', 'display_size')
        # fields = '__all__'