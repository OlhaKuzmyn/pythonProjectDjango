from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.jwt_service import JwtService, JwtServiceRecovery


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtService.validate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class ResetPasswordView(GenericAPIView):  # using url
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        new_password = kwargs.get('new_password')
        token = kwargs.get('token')
        user = JwtServiceRecovery.validate_token(token)
        user.set_password(new_password)
        user.save()
        return Response(status=status.HTTP_200_OK)
