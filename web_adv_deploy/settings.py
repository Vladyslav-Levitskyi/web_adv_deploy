from pathlib import Path
import dj_database_url
import os
from dotenv import load_dotenv
import logging


load_dotenv()

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
logger.info(f"SECRET_KEY: {SECRET_KEY}")

OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")
logger.info(f"OPENWEATHER_KEY: {OPENWEATHER_KEY}")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")
logger.info(f"DEBUG: {DEBUG}")

if DEBUG:
    # Локальне середовище
    ALLOWED_HOSTS = [
        "127.0.0.1",  # Локальний хост
        "localhost",   # Локальний хост
    ]
else:
    # Серверне середовище
    ALLOWED_HOSTS = [
        "web-adv-deploy.onrender.com",  # Домен на сервері
    ]

logger.info(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")


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
    #    'whitenoise.middleware.WhiteNoiseMiddleware',
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
    database_url = os.getenv("DATABASE_URL")
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



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core_app/static'),  # Вказуємо на директорію, де знаходяться статичні файли
]

# STATICFILES_DIRS = [
#     BASE_DIR / 'static/core_app/css',  
#     BASE_DIR / 'static/core_app/img',            
# ]


# Директорія, куди будуть зберігатися зібрані статичні файли
# STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.ManifestStaticFilesStorage'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


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