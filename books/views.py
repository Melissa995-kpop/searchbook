from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser  # 🔥 SHART!

# ✅ Custom foydalanuvchi modelini olamiz
User = get_user_model()

# 📚 Faqat egasi tahrirlashi yoki o‘chirishi mumkin bo‘lgan permission
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user

# 📚 API uchun ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# 🌐 HTML sahifa uchun view
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# 🔐 Register uchun serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # ✅ CustomUser ishlatilmoqda
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        ref_name = 'BookRegisterSerializer'

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

# 🔐 Register view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# ✅ Foydalanuvchining o‘z kitoblari uchun view
class MyBooksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.filter(owner=request.user)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
