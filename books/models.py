from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)  # Kitob nomi
    author = models.CharField(max_length=255)  # Muallif
    description = models.TextField(blank=True)  # Tavsif (ixtiyoriy)
    file = models.FileField(upload_to='books/')  # Yuklangan PDF
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Sana (avto)

    def __str__(self):
        return self.title

