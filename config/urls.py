from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

# 🔐 JWT import
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 📄 Swagger import
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 📄 Swagger sozlamasi
schema_view = get_schema_view(
    openapi.Info(
        title="SearchBook API",
        default_version='v1',
        description="Elektron kitoblar uchun API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', lambda request: redirect('schema-swagger-ui')),  # 🌐 Root sahifani Swaggerga redirect qiladi
    path('admin/', admin.site.urls),

    path('api/', include('books.urls')),  # 🔗 DRF API (JSON)
    path('books/', include('books.urls')),  # 🌐 HTML sahifalar uchun: /books/book-list/

    path('auth/', include('users.urls')),

    # 🔐 JWT token endpointlari
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📄 Swagger hujjatlari
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# 📂 Media va Static fayllar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

