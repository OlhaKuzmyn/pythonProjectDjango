from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.computer.models import ComputerModel
from apps.computer.serializers import ComputerSerializer


class ComputerListCreateView(APIView):
    def get(self, *args, **kwargs):
        computers = ComputerModel.objects.all()
        serializer = ComputerSerializer(computers, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ComputerSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ComputerUpdateRetrieveDestroyView(APIView):
    def get(self, *args, **kwargs):
        computer_id = kwargs.get('pk')
        if not ComputerModel.objects.filter(pk=computer_id).exists():
            return Response('Computer not found!', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=computer_id)
        serializer = ComputerSerializer(computer)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')
        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response('Computer not found!', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(computer, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        pk = kwargs.get('pk')
        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response('Computer not found!', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=pk)
        serializer = ComputerSerializer(computer, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        if not ComputerModel.objects.filter(pk=pk).exists():
            return Response('Computer not found!', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=pk)
        computer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
