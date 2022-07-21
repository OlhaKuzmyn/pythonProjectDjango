from django.contrib.auth import get_user_model

from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.cars.serializers import CarSerializer

from .filters import AutoParkFilter
from .models import AutoParkModel
from .serializers import AutoParkSerializer

UserModel = get_user_model()


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (AllowAny,)
    filterset_class = AutoParkFilter
    # def get_queryset(self):
    #     self.queryset.filter(cars__year__lt=)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owners=[user])


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


class AddOwnerToAutoParkView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer

    def patch(self, *args, **kwargs):
        user = self.request.user
        auto_park = self.get_object()
        user_id = kwargs.get('user_id')
        new_owner = get_object_or_404(UserModel, pk=user_id)
        if auto_park.owners.filter(pk=user.id).exists():
            auto_park.owners.add(new_owner)
        return Response(self.serializer_class(auto_park).data)