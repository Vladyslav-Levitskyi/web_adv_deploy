from pathlib import Path
import dj_database_url
import os
from dotenv import load_dotenv

#       Example for ensure safety with dotenv module:
#   from dotenv import load_dotenv
#
#   load_dotenv()
#   EXAMPLE = os.getenv("EXAMPLE")
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
OPENWEATHER_KEY = os.environ.get("OPENWEATHER_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "True") == "False"
#   ALLOWED_HOSTS = ["web_adv_deploy.onrender.com", "127.0.0.1"]
#   DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = [
    "web-adv-deploy.onrender.com",
    "127.0.0.1",
    "localhost"
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web_adv_deploy',
    'core_app',
    'register',
    'weather',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'web_adv_deploy.urls'

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
                'core_app.context_processors.weather_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_adv_deploy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if os.getenv("DJANGO_ENV") == "development":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
        }
    }
else:
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        DATABASES = {
            'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
        }
    else:
        raise ValueError("DATABASE_URL environment variable is not set")
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Налаштування статичних файлів для проекту Django
STATIC_URL = '/static/'

# Директорії, де Django буде шукати статичні файли
STATICFILES_DIRS = [
    BASE_DIR / 'core_app/static',  # Директорія для статичних файлів основного додатку
    BASE_DIR / 'register',          # Директорія для статичних файлів реєстрації
]

# Директорія, куди будуть зберігатися зібрані статичні файли
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# Використання WhiteNoise для обслуговування статичних файлів
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Додавання WhiteNoise до середовища

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}