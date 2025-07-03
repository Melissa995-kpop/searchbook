# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        ref_name = 'UserRegisterSerializer'  # Swagger uchun noyob nom

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Parollar mos emas!"})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  # password2 saqlanmaydi
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user





