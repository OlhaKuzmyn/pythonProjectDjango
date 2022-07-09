from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        authoParkId = self.request.query_params.get('authoParkId')
        if authoParkId:
            return self.queryset.filter(autho_park = authoParkId)
        return super().get_queryset()


class CarRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
