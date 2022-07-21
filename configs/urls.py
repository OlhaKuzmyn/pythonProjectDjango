"""configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.urls import include, path
from configs import settings
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="Autoparks API",
        default_version='v1',
        description="About cars",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('cars', include('apps.cars.urls')),
    path('autoparks', include('apps.autoparks.urls')),
    path('users', include('apps.users.urls')),
    path('auth', include('apps.auth.urls')),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0))
]

handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
