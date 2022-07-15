from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from core.permissions import IsSuperUser
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


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChangeSuperAdminUser
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)


