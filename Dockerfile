# 🔧 Rasm: Python 3.10 slim versiyasi
FROM python:3.10-slim

# 📌 Tizim yangilanishi va zarur OS kutubxonalar
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 📁 App uchun ishchi papka
WORKDIR /app

# 🧾 requirements.txt faylini konteynerga ko‘chirish
COPY requirements.txt .

# 📦 Python kutubxonalarni o‘rnatish
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Butun loyiha fayllarini konteynerga ko‘chirish
COPY . .

# 🔄 Statik fayllarni tayyorlash (collectstatic)
RUN python manage.py collectstatic --noinput

# 🌍 Port ochish
EXPOSE 8000

# 🚀 Konteyner ishga tushganda bajariladigan komanda
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
