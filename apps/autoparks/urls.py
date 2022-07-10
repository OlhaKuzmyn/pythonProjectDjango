from django.urls import path

from .views import AutoParkAddCarView, AutoParkListCreateView, AutoParksRetrieveUpdateDestroy

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>', AutoParksRetrieveUpdateDestroy.as_view()),
    path('/<int:pk>/car', AutoParkAddCarView.as_view()),
]