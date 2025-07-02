from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # 🔄 Root sahifa uchun redirect
from django.conf import settings
from django.conf.urls.static import static

# 🔐 JWT import
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),                          # ✅ Admin panel
    path('', lambda request: redirect('books/')),             # 🔄 Root ("/") ni /books/ ga yo'naltirish
    path('books/', include('books.urls')),                    # 📚 books app'ining URL-lari
    path('auth/', include('users.urls')),                     # ✅ Ro‘yxatdan o‘tish (register) URL-lari

    # 🔐 JWT login va refresh endpointlari
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),         # 🔑 Login: access + refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),        # ♻️ Token yangilash
]

# 📂 Media fayllarni ko‘rsatish (PDF yuklash uchun)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







