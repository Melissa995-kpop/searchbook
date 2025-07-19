from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    # Hech qanday qo‘shimcha maydon yo‘q, shuning uchun original fieldsets ishlatiladi
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets





