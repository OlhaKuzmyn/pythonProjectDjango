from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions import IsSuperUser
from core.services.email_service import EmailService
from core.services.jwt_service import JwtServiceRecovery

from .serializers import AddAvatarSerializer, ChangeSuperAdminUser, ResetPasswordSerializer, UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChangeSuperAdminUser
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)


class UserToAdminView(GenericAPIView):  # copied from 5th hw
    queryset = UserModel
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(UserToAdminView):  # copied from 5th hw
    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = self.serializer_class(user)
        return Response(serializer.data, status.HTTP_200_OK)


# class CheckEmailView(UserListCreateView):
#     # serializer_class = CheckEmailSerializer
#
#     def get_queryset(self):
#         email = self.request.query_params.get('email')
#         user_by_email = self.queryset.filter(email=email)
#         if user_by_email:
#             return user_by_email
#         return Response('Not found', status.HTTP_404_NOT_FOUND)
#
class CheckEmailView(GenericAPIView):
    queryset = UserModel
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'email'

    def get(self, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user)
        EmailService.reset_password(user)
        return Response(serializer.data, status.HTTP_200_OK)


class ResetPasswordView(GenericAPIView):  # using post
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, *args, **kwargs):
        new_password = self.request.data
        serializer = self.serializer_class(new_password)
        token = kwargs.get('token')
        user = JwtServiceRecovery.validate_token(token)
        user.set_password(serializer.data.get('password'))
        user.save()
        return Response(status.HTTP_200_OK)
