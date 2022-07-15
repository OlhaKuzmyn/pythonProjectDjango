from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateUserView, ResetPasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/reset/<str:token>/<str:new_password>', ResetPasswordView.as_view()),

]