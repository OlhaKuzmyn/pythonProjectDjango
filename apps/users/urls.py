from django.urls import path

from .views import (
    AddAvatarView,
    AdminToUserView,
    CheckEmailView,
    ResetPasswordView,
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/toadmin', UserToAdminView.as_view()),
    path('/<int:pk>/touser', AdminToUserView.as_view()),
    # path('/checkpassword', CheckEmailView.as_view())
    path('/checkpassword/<str:email>', CheckEmailView.as_view()),
    path('/changepass/<str:token>', ResetPasswordView.as_view())

]