import os

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST_SCHEME = 'https://'
PARENT_HOST = 'darkkeks-bots.herokuapp.com'
SITE_DOMAIN = HOST_SCHEME + PARENT_HOST

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get("DEBUG") is not None

ALLOWED_HOSTS = [
    '*'
]

ADMINS = [('DarkKeks', 'darkkeks@rambler.ru')]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bot_adapter.apps.BotConfig',
    'ornobot.apps.OrnobotConfig',
    'vkrepost.apps.VkRepostConfig'
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

ROOT_URLCONF = 'Bots.urls'

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

WSGI_APPLICATION = 'Bots.wsgi.application'

DATABASES = {
    'default': dj_database_url.config()
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

ORNOBOT_TOKEN = os.environ.get('ORNOBOT_TOKEN')

VKREPOST_TOKEN = os.environ.get('VKREPOST_TOKEN')
VKREPOST_VK_TOKEN = os.environ.get('VKREPOST_VK_TOKEN')
