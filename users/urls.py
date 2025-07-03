from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 🆕 Ro'yxatdan o'tish
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 🔐 Login (access + refresh token)
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ♻️ Token yangilash
]



