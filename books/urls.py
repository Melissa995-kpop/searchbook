from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, book_list_view, RegisterView, MyBooksView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),  # API router orqali barcha DRF endpointlar
    path('book-list/', book_list_view, name='book_list'),  # ✅ HTML sahifa ko‘rsatadigan view
    path('register/', RegisterView.as_view(), name='register'),
    path('my-books/', MyBooksView.as_view(), name='my_books'),

    # JWT token auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]








