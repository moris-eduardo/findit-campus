# FindIt/FindIt/settings.py
# FindIt Campus — FIME UANL
#
# CAMBIOS respecto al settings.py original:
# 1. Se agregó PostgreSQL (con SQLite como fallback para desarrollo)
# 2. Se agregaron las apps: DRF, JWT, CORS, cloudinary, y las nuestras
# 3. Se configuró AUTH_USER_MODEL para usar nuestro User personalizado
# 4. Se agregó configuración de JWT y CORS para conectar con React
# 5. Idioma cambiado a español México y zona horaria a Monterrey



from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Seguridad ──────────────────────────────────────────────────────────────
SECRET_KEY = os.getenv('SECRET_KEY', 'clave-desarrollo-insegura-cambiar-en-produccion')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# ── Aplicaciones ───────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Librerías externas
    'rest_framework',            # API REST
    'rest_framework_simplejwt',  # Autenticación JWT
    'corsheaders',               # Permite que React hable con Django
    'django_filters',            # Filtros de búsqueda (categoría, color, zona)
    'cloudinary',                # Almacenamiento de imágenes
    'cloudinary_storage',        # Integración Cloudinary con Django

    # Nuestras apps
    'users',
    'items',
    'claims',
    'reports',
]

# ── Middleware ─────────────────────────────────────────────────────────────
# CorsMiddleware DEBE ir primero
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FindIt.urls'

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

WSGI_APPLICATION = 'FindIt.wsgi.application'

# ── Base de datos ──────────────────────────────────────────────────────────
# Usamos PostgreSQL. Si no tienes PostgreSQL instalado aún,
# cambia ENGINE a 'django.db.backends.sqlite3' y NAME a BASE_DIR / 'db.sqlite3'
# para desarrollo local mientras lo instalas.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':     os.getenv('DB_NAME',     'findit_campus'),
        'USER':     os.getenv('DB_USER',     'root'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),
        'HOST':     os.getenv('DB_HOST',     'localhost'),
        'PORT':     os.getenv('DB_PORT',     '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

# ── Modelo de usuario personalizado ───────────────────────────────────────
# Le dice a Django que use NUESTRO modelo User (users/models.py)
# en vez del que trae Django por defecto.
# IMPORTANTE: esto debe definirse ANTES de correr migrate por primera vez.
AUTH_USER_MODEL = 'users.User'

# ── Django REST Framework ──────────────────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
}

# ── JWT — tokens de autenticación ─────────────────────────────────────────
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME':  timedelta(minutes=15),  # Expira rápido por seguridad
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),       # Refresh dura 7 días
    'ROTATE_REFRESH_TOKENS':  True,                    # Genera nuevo refresh en cada uso
    'AUTH_HEADER_TYPES':      ('Bearer',),
}

# ── CORS — permite que React (Vite) hable con Django ──────────────────────
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',   # React + Vite (desarrollo)
    'http://localhost:3000',   # React alternativo
]
CORS_ALLOW_CREDENTIALS = True

# ── Cloudinary — imágenes de objetos ──────────────────────────────────────
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', ''),
    'API_KEY':    os.getenv('CLOUDINARY_API_KEY',    ''),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', ''),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ── Validación de contraseñas ──────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Configuración regional ─────────────────────────────────────────────────
LANGUAGE_CODE = 'es-mx'
TIME_ZONE     = 'America/Monterrey'
USE_I18N      = True
USE_TZ        = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'