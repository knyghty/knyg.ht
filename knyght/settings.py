import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['.knyg.ht']
APPEND_SLASH = False

IGNORABLE_404_URLS = (
    'robots.txt',
    'favicon.ico',
)

ADMINS = (
    ('Tom Carrick', 'knyght@knyg.ht'),
)

MANAGERS = ADMINS


if DEBUG:
    SECRET_KEY = 'debug'
else:
    with open('/etc/secret_key') as f:
        SECRET_KEY = f.read().strip()


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mptt',
    'pages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
)

ROOT_URLCONF = 'knyght.urls'
WSGI_APPLICATION = 'knyght.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Context Processors

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'pages.context_processors.nav',
)


# Internationalization

TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/common'),
)

STATIC_URL = '/static/'
STATIC_ROOT = '/usr/local/www/static/'


# Templates

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)
