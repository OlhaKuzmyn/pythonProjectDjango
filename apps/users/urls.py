from django.urls import path

from .views import AddAvatarView, AdminToUserView, UserListCreateView, UserRetrieveUpdateDestroyView, UserToAdminView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/avatars', AddAvatarView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/toadmin', UserToAdminView.as_view()),
    path('/<int:pk>/touser', AdminToUserView.as_view())

]