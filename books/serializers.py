from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)  # ✅ Foydalanuvchi nomi ko‘rinadi

    class Meta:
        model = Book
        fields = '__all__'

