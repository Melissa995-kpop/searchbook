from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer

# 📚 API uchun ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# 🌐 HTML sahifa uchun view
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# 🔐 Register uchun serializer
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

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





