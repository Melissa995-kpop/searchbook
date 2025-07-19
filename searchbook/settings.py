import os
from pathlib import Path
from datetime import timedelta

# 📌 Bazaviy yo‘l
BASE_DIR = Path(__file__).resolve().parent.parent

# 📌 Xavfsizlik kaliti (faqat local test uchun)
SECRET_KEY = 'django-insecure-1234567890-very-insecure-key-for-dev-only'

# 📌 Ishlab chiqish holati
DEBUG = True

# 📌 Ruxsat etilgan hostlar
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'searchbook-1-mt61.onrender.com',  # Render.com domeni
]

# 📌 Ilovalar
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd-party apps
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',

    # Custom apps
    'books',
    'accounts',
]

# 📌 Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 🔥 CORS middleware eng yuqorida bo‘lishi shart
    'django.middleware.common.CommonMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 📌 URL konfiguratsiyasi
ROOT_URLCONF = 'searchbook.urls'

# 📌 Templateler
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 📌 WSGI
WSGI_APPLICATION = 'searchbook.wsgi.application'

# 📌 Ma’lumotlar bazasi (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 📌 Parol validatsiyasi
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 📌 Til va vaqt
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📌 Statik va media fayllar
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 📌 Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📌 Custom foydalanuvchi modeli
AUTH_USER_MODEL = 'accounts.CustomUser'

# 📌 DRF + JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# 📌 Swagger sozlamalari
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        }
    },
}

# 📌 CORS sozlamalari
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# 📌 HTTPS uchun sozlama (Render.com uchun kerak)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
