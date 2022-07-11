from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        autoParkId = self.request.query_params.get('autoParkId')
        if autoParkId:
            return self.queryset.filter(auto_park=autoParkId)
        return super().get_queryset()


class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
