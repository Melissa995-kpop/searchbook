from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, book_list_view, RegisterView  # ✅ RegisterView ham import qilindi

# 📚 DRF router yaratamiz
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# 🔗 URL patterns
urlpatterns = [
    path('', include(router.urls)),                          # ✅ API endpointlar: /books/
    path('book-list/', book_list_view, name='book_list'),    # ✅ HTML sahifa: /book-list/
    path('register/', RegisterView.as_view(), name='register'),  # ✅ Register endpoint: /register/
]





