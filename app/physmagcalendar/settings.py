"""
Django settings for physmagcalendar project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from decouple import config,  UndefinedValueError
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'testserver',
    '.physiquemagnifique.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Native Apps
    'home',
    'fitness',
    'oweightlifting',
    'boxing',
    'studio'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'physmagcalendar.urls'

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

WSGI_APPLICATION = 'physmagcalendar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

try:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DBNAME', default=''),
            'USER': config('DBUSER', default=''),
            'PASSWORD': config('DBPWD', default=''),
            'HOST': config('DBHOST', default='localhost'),
            'PORT': config('DBPORT', default='5432'),
        }
    }
except UndefinedValueError as e:
    raise ImproperlyConfigured(f"Missing database configuration: {e}") from e


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

MY_PROJECT_STATIC_FILES = os.path.join(BASE_DIR, 'static')
REACT = os.path.join(BASE_DIR, 'static', 'react')

# URL to use when referring to static files located in STATIC_ROOT.
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# The absolute path to the directory where collectstatic will collect static files for deployment.
# https://docs.djangoproject.com/en/4.2/howto/static-files/#deployment

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# List of all static file directory locations
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STATICFILES_DIRS

STATICFILES_DIRS = [
    MY_PROJECT_STATIC_FILES,
    REACT
]

# Compression and Caching support for static files
# https://whitenoise.readthedocs.io/en/stable/django.html#add-compression-and-caching-support

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Google Calendar APIs

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CSRF Tokens
# https://docs.djangoproject.com/en/4.2/howto/csrf/

CSRF_TRUSTED_ORIGINS = ['https://calendar.physiquemagnifique.com','http://127.0.0.1:8000']

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

# FullCalendar Secrets
# https://fullcalendar.io/

GOOGLE_CREDS = os.path.join(BASE_DIR, 'credentials.json')
BOXING_CALENDAR_ID = config('BOXING_CALENDAR_ID')
STUDIO_CALENDAR_ID = config('STUDIO_CALENDAR_ID')
FITNESS_CALENDAR_ID = config('FITNESS_CALENDAR_ID')
OWEIGHTLIFTING_CALENDAR_ID = config('OWEIGHTLIFTING_CALENDAR_ID')
VONS_PRIVATES_ID = config('VONS_PRIVATES_ID')
