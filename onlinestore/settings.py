"""
Django settings for onlinestore project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import environ
from celery.schedules import crontab
from django.template.context_processors import media
from django.urls import reverse_lazy

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hhs5yc6+aw(h3&4f+(mayrom)go1ofc51a&8#9=_@!1x=g0&cm'  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=True)
DOMAIN = env('DOMAIN', default='127.0.0.1:8888')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #external apps
    'django_extensions',
    'django_celery_results',
    #My apps
    'products',
    'main',
    'orders',
    'feedbacks',
    'users',
    'tracking',
    'currencies',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'onlinestore.urls'
APPEND_SLASH = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'onlinestore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
STATICFILES_DIRS = ['static_dev']

MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = reverse_lazy('main')
LOGIN_REDIRECT_URL = reverse_lazy('main')
LOGIN_URL = reverse_lazy('login')


CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = 'django_celery_results.backends.database.DatabaseBackend' #noqa
CELERY_IMPORTS = ("onlinestore.tasks",)
CELERY_BEAT_SCHEDULE = {
    'Get currency': {
        'task': 'currencies.tasks.get_currencies',
        'schedule': crontab(hour='9', minute='1')
    },
}

CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': env('MEMCACHE_LOCATION', default='MEMCACHE_LOCATION'),
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'django_cache',
    }
}