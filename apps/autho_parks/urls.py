from django.urls import path

from .views import AuthoParkListCreateView, AuthoParksRetrieveUpdateDestroy, AuthoParkAddCarView

urlpatterns = [
    path('', AuthoParkListCreateView.as_view()),
    path('/<int:pk>', AuthoParksRetrieveUpdateDestroy.as_view()),
    path('/<int:pk>/car', AuthoParkAddCarView.as_view()),

]