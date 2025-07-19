from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, RegisterView, MyBooksView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # 🔐 JWT login/logout/register
    path('users/register/', RegisterView.as_view(), name='api_users_register_create'),
    path('users/login/', TokenObtainPairView.as_view(), name='api_users_login_create'),
    path('users/refresh/', TokenRefreshView.as_view(), name='api_users_refresh_create'),

    # ✅ Foydalanuvchining o'z kitoblari
    path('users/mybooks/', MyBooksView.as_view(), name='api_users_mybooks_list'),
]
