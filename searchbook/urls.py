from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SearchBook API",
        default_version='v1',
        description="Elektron kitoblar uchun API hujjatlari",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # 🔹 Bosh sahifa Swagger UI’ga yo‘naltiradi
    path('', lambda request: redirect('schema-swagger-ui')),

    # 🔹 Admin
    path('admin/', admin.site.urls),

    # 🔹 API
    path('api/', include('books.urls')),
    path('auth/', include('accounts.urls')),

    # ✅ Swagger JSON / YAML formatlar (drf-yasg style)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # ✅ Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ✅ ReDoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # ✅ Swagger JSON (asosiy /swagger.json URL uchun qo‘shimcha)
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='swagger-json-direct'),
]

# 🔹 Static fayllar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
