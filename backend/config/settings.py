"""
Django settings for config project.
"""

from pathlib import Path


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Security
SECRET_KEY = 'django-insecure-si*iykf^^dj6=6_1+w!ra&^73@v)m^r_1qv2)xxyv8v8xe6a6k'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    'corsheaders',

    # Local apps
    'bares',
]


# Django REST Framework

REST_FRAMEWORK = {

    'DEFAULT_SCHEMA_CLASS':
        'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_FILTER_BACKENDS': [

        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',

    ],

    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 10,
}


# Swagger / OpenAPI

SPECTACULAR_SETTINGS = {

    'TITLE': 'SevillaPlan API',

    'DESCRIPTION': (
        'API REST de SevillaPlan para consultar, filtrar, buscar y gestionar '
        'bares y futuros lugares de interés de Sevilla.'
    ),

    'VERSION': '1.0.0',

    'CONTACT': {
        'name': 'José Ángel Carrión',
    },

    'LICENSE': {
        'name': 'Uso académico',
    },
}


# Middleware

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


ROOT_URLCONF = 'config.urls'


# Templates

TEMPLATES = [

    {

        'BACKEND':
            'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]


WSGI_APPLICATION = 'config.wsgi.application'


# Database

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'bares_sevilla',

        'USER': 'root',

        'PASSWORD': 'Sevillano94',

        'HOST': 'localhost',

        'PORT': '3306',

    }

}


# Password validation

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files

STATIC_URL = 'static/'


# CORS React

CORS_ALLOWED_ORIGINS = [

    "http://localhost:5173",

]