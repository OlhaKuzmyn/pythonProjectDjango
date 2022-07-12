from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from permissions.user_permissions import IsSuperUser
from .serializers import AddAvatarSerializer, UserSerializer, ChangeSuperAdminUser

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)


class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile


class ChangeSuperAdminUserView(UpdateAPIView):
    serializer_class = ChangeSuperAdminUser
    permission_classes = IsSuperUser

    def get_object(self):
        return self.request.user

