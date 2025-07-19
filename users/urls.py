# users/urls.py
from django.urls import path
from books.views import RegisterView, MyBooksView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 🆕 Ro‘yxatdan o‘tish
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 🔐 Login
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ♻️ Token yangilash
    path('mybooks/', MyBooksView.as_view(), name='my_books'),  # 🗂️ Foydalanuvchining kitoblari
]



