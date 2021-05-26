# -*- coding: utf-8 -*-
"""
Django settings for cloud_spirit project.

Generated by 'django-admin startproject' using Django 3.1.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from dotenv import load_dotenv

# Env variable configurations
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'spirit.core',
    'spirit.admin',
    'spirit.search',

    'spirit.user',
    'spirit.user.admin',
    'spirit.user.auth',

    'spirit.category',
    'spirit.category.admin',

    'spirit.topic',
    'spirit.topic.admin',
    'spirit.topic.favorite',
    'spirit.topic.moderate',
    'spirit.topic.notification',
    'spirit.topic.private',
    'spirit.topic.unread',

    'spirit.comment',
    'spirit.comment.bookmark',
    'spirit.comment.flag',
    'spirit.comment.flag.admin',
    'spirit.comment.history',
    'spirit.comment.like',
    'spirit.comment.poll',

    'djconfig',
    'haystack',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'spirit.core.middleware.XForwardedForMiddleware',
    'spirit.user.middleware.TimezoneMiddleware',
    'spirit.user.middleware.LastIPMiddleware',
    'spirit.user.middleware.LastSeenMiddleware',
    'spirit.user.middleware.ActiveUserMiddleware',
    'spirit.core.middleware.PrivateForumMiddleware',
    'djconfig.middleware.DjConfigMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'djconfig.context_processors.config',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'spirit_cache',
    },
    'st_rate_limit': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'spirit_rl_cache',
        'TIMEOUT': None
    }
}

AUTHENTICATION_BACKENDS = [
    'spirit.user.auth.backends.UsernameAuthBackend',
    'spirit.user.auth.backends.EmailAuthBackend',
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'st_search'),
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'spirit.search.signals.RealtimeSignalProcessor'

ROOT_URLCONF = 'cloud_spirit.urls'

WSGI_APPLICATION = 'cloud_spirit.wsgi.application'

LOGIN_URL = 'spirit:user:auth:login'
LOGIN_REDIRECT_URL = 'spirit:user:update'
LOGOUT_REDIRECT_URL = 'spirit:index'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'spirit.core.storage.OverwriteFileSystemStorage'


# Send an email to the site admins
# on error when DEBUG=False,
# log to console on error always.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
#         },
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['require_debug_false'],
#             'formatter': 'verbose',
#             'level': 'ERROR',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'django.log'),
#             'formatter': 'verbose',
#             'level': 'ERROR',
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#     },
#     'loggers': {
#         '': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         'django': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'celery': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'INFO',
#             'propagate': False
#         },
#         'huey': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'INFO',
#             'propagate': False
#         },
#     }
# }

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#admins
ADMINS = (('John', 'john@example.com'), )

SECRET_KEY = os.environ.get("SECRET_KEY", 'ka81%we_2@zw0qeq4%yspzd2^93%=a_b2n)z7^z8d9!z@su4y5')

# https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# You can change this to something like 'MyForum <noreply@example.com>'
DEFAULT_FROM_EMAIL = 'webmaster@localhost'  # Django default
SERVER_EMAIL = DEFAULT_FROM_EMAIL  # For error notifications

# Email sending timeout
EMAIL_TIMEOUT = 20  # Default is None (infinite)

# Extend the Spirit installed apps
# Check out the .base.py file for more examples
INSTALLED_APPS.extend([
    # 'huey.contrib.djhuey',
])

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'mydatabase'),
        'USER': os.environ.get('DB_USER', 'mydatabaseuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'mypassword'),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# These are all the languages Spirit provides.
# https://www.transifex.com/projects/p/spirit/
gettext_noop = lambda s: s
LANGUAGES = [
    ('de', gettext_noop('German')),
    ('en', gettext_noop('English')),
    ('es', gettext_noop('Spanish')),
    ('fr', gettext_noop('French')),
    ('hu', gettext_noop('Hungarian')),
    ('it', gettext_noop('Italian')),
    ('ky', gettext_noop('Kyrgyz')),
    ('lt', gettext_noop('Lithuanian')),
    ('pl', gettext_noop('Polish')),
    ('pl-pl', gettext_noop('Poland Polish')),
    ('ru', gettext_noop('Russian')),
    ('sv', gettext_noop('Swedish')),
    ('tr', gettext_noop('Turkish')),
    ('zh-hans', gettext_noop('Simplified Chinese')),
]

# Default language
LANGUAGE_CODE = 'en'

# Append the MD5 hash of the file’s content to the filename
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Celery is optional, Huey can be used instead
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
# https://docs.celeryproject.org/en/latest/userguide/configuration.html
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_BEAT_SCHEDULE = {
    'notify_weekly': {
        'task': 'spirit.core.tasks.notify_weekly',
        'schedule': 3600 * 24 * 7  # run once every week
        # 'schedule': crontab(hour=0, minute=0, day_of_week='sun')
    },
    'full_search_index_update': {
        'task': 'spirit.core.tasks.full_search_index_update',
        'schedule': 3600 * 24  # run once every 24hs
    }
}

# Huey
# https://huey.readthedocs.io/en/latest/django.html
HUEY = {
    'huey_class': 'huey.RedisHuey',
    'name': 'spirit',
    'immediate_use_memory': False,
    'immediate': False,
    'utc': True,
    'blocking': True,
    'connection': {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
        'max_connections': 500,  # Pooling
        # ... tons of other options, see redis-py for details.
        # huey-specific connection parameters.
        'read_timeout': 1,
        'url': None,  # Allow Redis config via a DSN.
    },
    'consumer': {
        'workers': os.cpu_count() * 2 + 1,
        'worker_type': 'thread',
        'initial_delay': 0.1,
        'backoff': 1.15,
        'max_delay': 10.0,
        'scheduler_interval': 1,
        'periodic': True,
        'check_worker_health': True,
        'health_check_interval': 1,
    }
}

# https://spirit.readthedocs.io/en/latest/settings.html#spirit.core.conf.defaults.ST_SITE_URL
ST_SITE_URL = 'https://example.com/'
