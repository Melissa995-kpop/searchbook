from django.db import models
from django.conf import settings  # ✅ AUTH_USER_MODEL uchun

class Book(models.Model):
    title = models.CharField(max_length=255)  # Kitob nomi
    author = models.CharField(max_length=255)  # Muallif
    description = models.TextField(blank=True)  # Tavsif (ixtiyoriy)
    file = models.FileField(upload_to='books/')  # Yuklangan PDF
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Sana (avto)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books')  # ✅ Custom foydalanuvchi

    def __str__(self):
        return str(self.title)



