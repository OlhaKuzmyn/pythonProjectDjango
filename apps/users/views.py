from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions import IsSuperUser

from .serializers import AddAvatarSerializer, ChangeSuperAdminUser, UserSerializer

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
