from django.urls import path

from .views import AddOwnerToAutoParkView, AutoParkAddCarView, AutoParkListCreateView, AutoParksRetrieveUpdateDestroy

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>', AutoParksRetrieveUpdateDestroy.as_view()),
    path('/<int:pk>/car', AutoParkAddCarView.as_view()),
    path('/<int:pk>/add_owner/<int:user_id>', AddOwnerToAutoParkView.as_view())
]