from pathlib import Path
import os

# 📁 Bazaviy yo‘l
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Xavfsizlik kaliti (faqat test uchun!)
SECRET_KEY = 'django-insecure-1234567890-very-insecure-key-for-dev-only'

# 🔧 Ishlab chiqish holati
DEBUG = True

# 🌐 Ruxsat berilgan hostlar
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# 📦 Ilovalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ REST va Swagger
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',

    # 📚 Loyihangdagi app'lar
    'books',
    'accounts',  # 🔁 oldingi 'users' o‘rniga
]

# ⚙️ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔗 URL konfiguratsiyasi
ROOT_URLCONF = 'config.urls'

# 🧩 Templateler
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

# 🔌 WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# 🗃️ SQLite bazasi
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔒 Parol tekshiruvlar
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 🌍 Til va vaqt
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📁 Statik fayllar (CSS, JS)
STATIC_URL = 'static/'

# 📂 Media fayllar (PDF, rasm, va h.k.)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 🆔 Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ JWT autentifikatsiyasi
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# ✅ Swagger sozlamalari
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

# 🔐 Custom foydalanuvchi model
AUTH_USER_MODEL = 'accounts.CustomUser'