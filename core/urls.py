from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from django.views.generic import RedirectView

schema_view = get_schema_view(openapi.Info(
      title="Crypto API",
      default_version='v1',
      description="",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("crypto.urls")),
    re_path(r'^api/v1/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('', RedirectView.as_view(url='api/v1/docs/'))


]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)