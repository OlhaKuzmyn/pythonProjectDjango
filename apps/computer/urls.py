from django.urls import path

from apps.computer.views import ComputerListCreateView
from apps.computer.views import ComputerUpdateRetrieveDestroyView

urlpatterns = [
    path('', ComputerListCreateView.as_view()),
    path('/<int:pk>', ComputerUpdateRetrieveDestroyView.as_view())
]
