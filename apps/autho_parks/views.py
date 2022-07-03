from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import AuthoParkModel
from .serializers import AuthoParkSerializer
from apps.cars.serializers import CarSerializer


class AuthoParkListCreateView(ListCreateAPIView):
    queryset = AuthoParkModel.objects.all()
    serializer_class = AuthoParkSerializer


class AuthoParksRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthoParkSerializer
    queryset = AuthoParkModel.objects.all()


class AuthoParkAddCarView(CreateAPIView):
    queryset = AuthoParkModel
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        autho_park = self.get_object()
        serializer.save(autho_park=autho_park)
