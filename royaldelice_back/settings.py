"""
Django settings for royaldelice_back project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime
import os
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(8(4@g*jxd2ec003mv$f!!=!^(+y%mmnnmwoml(ecoqkn82hw0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "*",
    "127.0.0.1:8000",
    "https://royaldelice.herokuapp.com/"

]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restaurant.apps.RestaurantConfig',
    'paiement.apps.PaiementConfig',
    'comptabilite.apps.ComptabiliteConfig',
    'accounts.apps.AccountsConfig',
    'main.apps.MainConfig',
    'django_rest_passwordreset',
    'rest_framework',
    'corsheaders',  # cors
    'django_filters',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    # Cors
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hhezv16sv',
    'API_KEY': '538375941866213',
    'API_SECRET': '4RbhT2kJSgZmTWeK-qNmM1rEHNE',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

ROOT_URLCONF = 'royaldelice_back.urls'

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

REST_FRAMEWORK = {
    'DATE_INPUT_FORMATS': '%d/%m/%Y',
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    )
}

WSGI_APPLICATION = 'royaldelice_back.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Sql lite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

# MySql
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'OPTIONS': {
#            'database': 'lescrocsdelanight-restaurant',
#            'password': '',
#            'user': 'root',
#            'port': 3309,
#            'host': '127.0.0.1'  # 'localhost'
#        }
#    }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=15),
    'JWT_ALLOW_REFRESH': True,
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.views.custom_jwt.jwt_response_payload_handler',
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=15),
    # Authorization:Token xxx
    'JWT_AUTH_HEADER_PREFIX': 'Token',
}
SIMPLE_JWT = {
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=15),
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=15),
    'ROTATE_REFRESH_TOKENS': True,
}

# keys from Stripe API (final product)
#STRIPE_PUBLIC_KEY = "pk_live_5LbTSWNzdQ3stwG1bJOI7J9T00P1Iyi9EW"
#STRIPE_SECRET_KEY = "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"
#STRIPE_WEBHOOK_SECRET = ""

# test keys
STRIPE_PUBLIC_KEY = "pk_test_51K98MqDO5HJcx2Oda0dSkyVC6ild9Z4AH5IFLE03x9beV6EGZsaBEgzuMhtq5W6gCEL14kpb9nyhADyxQd7OpXM5005fEyslOD"
STRIPE_SECRET_KEY = "sk_test_51K98MqDO5HJcx2OdeETQOYH6PWseT4V1CmlTT9o2U9kcLhp2sbzwsIf7y32K4Hyx8fU54IBjwzKNSEMQsi8Ivd0X006ou1YM5y"


# STATIC_ROOT = Path(BASE_DIR) / 'staticfiles'
# os.path.join(BASE_DIR , 'staticfiles')
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

#  keys from Google maps API
# GOOGLE_MAPS_KEY = "AIzaSyD7HbeMdlKP2HldABmvuKlX8TRrTSKpq8g"

# Activate Django-Heroku.
django_heroku.settings(locals())
# off sslmode
# del DATABASES['default']['OPTIONS']['sslmode']
