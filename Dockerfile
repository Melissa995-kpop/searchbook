# 🔧 Python image asosida
FROM python:3.10-slim

# 📁 Ishchi katalog yaratish
WORKDIR /app

# 🧾 Talablar faylini nusxalash
COPY requirements.txt .

# 📦 Kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

# 🔁 Loyiha fayllarini konteynerga nusxalash
COPY . .

# 🔥 Django runserver komandasi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
