import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR_LOCAL = os.path.join(Path.home(), 'TaskRunner/data')
print(f'TASKRUNNER_DATA_DIR_LOCAL = {DATA_DIR_LOCAL}')

DATA_DIR = os.environ.get('DATA_DIR', DATA_DIR_LOCAL)
print(f'TASKRUNNER_DATA_DIR = {DATA_DIR}')

SECRET_KEY = os.environ.get('TASKRUNNER_SECRET_KEY', '1234')
print(f'TASKRUNNER_SECRET_KEY = {SECRET_KEY}')

DEBUG = os.environ.get('TASKRUNNER_DEBUG', 'true')
DEBUG = True if DEBUG == 'true' else False
print(f'TASKRUNNER_DEBUG = {DEBUG}')

ALLOWED_HOSTS = []

ADMIN_USER = os.getenv('TASKRUNNER_ADMIN_USER', 'admin')
ADMIN_PASSWORD = os.getenv('TASKRUNNER_ADMIN_PASSWORD', 'admin')
print(f'TASKRUNNER_ADMIN_USER = {ADMIN_USER}, TASKRUNNER_ADMIN_PASSWORD = {ADMIN_PASSWORD}')

SITE_ID = 1

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'session_security',
    'crispy_forms',
    'crispy_bootstrap5',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'taskrunner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'taskrunner.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'taskrunner': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
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

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

MEDIA_URL = '/filesets/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'filesets')

DATA_UPLOAD_MAX_NUMBER_FILES = None

FILE_UPLOAD_MAX_MEMORY_SIZE = 0

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SESSION_SECURITY_WARN_AFTER = 840
SESSION_SECURITY_EXPIRE_AFTER = 3600
SESSION_EXPIRE_AT_BROWSER_CLOSE = True