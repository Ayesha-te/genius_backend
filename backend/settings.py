import os
from pathlib import Path
from decouple import config
import dj_database_url

# --------------------
# Environment Variables
# --------------------
DVLA_API_URL = config('DVLA_API_URL')
DVLA_API_KEY = config('DVLA_API_KEY')
SECRET_KEY = config('SECRET_KEY', default='your-secret-key')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

# --------------------
# Paths
# --------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------
# Installed Apps
# --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd-party
    'rest_framework',
    'rest_framework.authtoken',

    # Your apps
    'booking',
    'support',
]

# --------------------
# Middleware
# --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Optionally disable CSRF middleware below if using TokenAuth only
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# --------------------
# Django REST Framework Settings
# --------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # ❌ Do NOT use SessionAuthentication if you want to avoid CSRF 403 errors
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Use IsAuthenticated if needed
    ]
}

# --------------------
# Database (PostgreSQL via Neon)
# --------------------
DATABASES = {
    'default': dj_database_url.parse(
        config('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# --------------------
# Templates
# --------------------
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

# --------------------
# URLs & WSGI
# --------------------
ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'

# --------------------
# Time and Language
# --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------
# Static Files
# --------------------
STATIC_URL = 'static/'

# --------------------
# Default Primary Key Field
# --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
