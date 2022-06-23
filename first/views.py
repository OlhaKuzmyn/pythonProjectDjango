from rest_framework.views import APIView
from rest_framework.response import Response


class FirstView(APIView):
    def get(self, request):
        return Response('Method GET')

    def post(self, request):
        return Response('Method POST')

    def put(self, request):
        return Response('Method PUT')

    def patch(self, request):
        return Response('Method PATCH')

    def delete(self, request):
        return Response('Method DELETE')
