from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.cars.serializers import CarSerializer

from .filters import AutoParkFilter
from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (AllowAny,)
    filterset_class = AutoParkFilter
    # def get_queryset(self):
    #     self.queryset.filter(cars__year__lt=)


class AutoParksRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializer
    queryset = AutoParkModel.objects.all()
    permission_classes = (AllowAny,)


class AutoParkAddCarView(CreateAPIView):
    queryset = AutoParkModel
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(auto_park=auto_park)
