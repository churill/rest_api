import os
import datetime
import pprint

import django
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str
from django.utils.translation import gettext
django.utils.translation.ugettext = gettext

import environ


env = environ.Env()

READ_ENV_FILE = env.bool('DJANGO_SETTINGS_READ_ENV_FILE', default=False)
if READ_ENV_FILE:
    env.read_env('.env')


###############
# Build paths #
###############

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_NAME = os.path.basename(BASE_DIR)

SITE_ID = 1


############
# Security #
############

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env.get_value('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


#################
# Core settings #
#################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    # My Applications
    'accounts.apps.AccountsConfig',
    'myapp_1.apps.Myapp1Config',
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
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dist')],
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

WSGI_APPLICATION = 'server.wsgi.application'


############
# Database #
############

# environ.Env.DB_SCHEMES['mssql'] = 'mssql'

DATABASES = {
    'default': env.db('DATABASE_URL')
}
# DATABASES['default'].update({
#     'OPTIONS': {
#         'driver': env.get_value('DATABASE_OPTIONS1'),
#         'extra_params': env.get_value('DATABASE_OPTIONS2')
#     }
# })

DATABASE_COUNT = env.int('DATABASE_COUNT', default=1)

for i in range(1, DATABASE_COUNT):
    DATABASES['database_{}'.format(i)] = env.db('DATABASE{}_URL'.format(i))
    # DATABASES['database_{}'.format(i)].update({
    #     'OPTIONS': {
    #         'driver': env('DATABASE{}_OPTIONS1'.format(i)),
    #         'extra_params': env('DATABASE{}_OPTIONS2'.format(i)),
    #     }
    # })

DATABASE_ROUTERS = ['server.router.DBRouter']


############
# Messages #
############

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


###########
# Logging #
###########

LOGGING = {}


##################
# Authentication #
##################

AUTH_USER_MODEL = 'accounts.CustomUser'


#######################
# Password validation #
#######################

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


########################
# Internationalization #
########################

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


################
# Static files #
################

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


##################################
# Default primary key field type #
##################################

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


########################
# Application settings #
########################

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=1),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=20),
}

CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST')