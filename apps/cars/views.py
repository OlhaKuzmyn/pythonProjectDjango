from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from core.permissions import IsSuperUser

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    # permission_classes = (AllowAny,)
    # permission_classes = (IsAdminUser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filterset_class = CarFilter

    def get_queryset(self):
        # self.queryset.filter(auto_park=)
        autoParkId = self.request.query_params.get('autoParkId')
        if autoParkId:
            return self.queryset.filter(auto_park=autoParkId)
        return super().get_queryset()


class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (IsSuperUser,)
    # permission_classes = (AllowAny,)
