"""
Django settings for openstudyroom project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from machina import get_apps as get_machina_apps
from machina import MACHINA_MAIN_TEMPLATE_DIR
from machina import MACHINA_MAIN_STATIC_DIR

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'home',
    'search',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #for django-user-account and puput and forum...
    'django.contrib.sites',

    #league app
    'league',

    #wgo
    'wgo',

    #for wagtailmenu
    'wagtail.contrib.modeladmin',
    'wagtailmenus',


    #
    'bootstrap3',

    #for puput
    'puput',
    'compressor',
    'wagtail.contrib.wagtailsitemaps',
    'wagtail.contrib.wagtailroutablepage',

    #allauth
    'allauth',
    'allauth.account',
    #'allauth.socialaccount',


    #django cron
    'django_cron',

    # Machina related apps:
    'mptt',
    'haystack',
    'widget_tweaks',

    #'django_messages',
    'postman',
    'django_countries',

    'fullcalendar',

    'community',
    'tournament',


    #for sentry
    'raven.contrib.django.raven_compat',

    'discord_bind',
    #"anymail",
    'stats'

]+ get_machina_apps()

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'openstudyroom.middleware.OSRLocaleMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

    # Machina
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
    'league.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'openstudyroom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
            MACHINA_MAIN_TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #for wagtailmenus
                'wagtailmenus.context_processors.wagtailmenus',
                #for django-messages
                #'django_messages.context_processors.inbox',
                'postman.context_processors.inbox',

                # Machina
                'machina.core.context_processors.metadata',

                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'openstudyroom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
    MACHINA_MAIN_STATIC_DIR,
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Wagtail settings

WAGTAIL_SITE_NAME = "openstudyroom"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://openstudyroom.org'

ALLOWED_HOSTS = ['127.0.0.1']

#do that before migrate
AUTH_USER_MODEL = 'league.User'

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

SITE_ID = 1

PUPUT_AS_PLUGIN = True

# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
ACCOUNT_FORMS = {}
ACCOUNT_SIGNUP_FORM_CLASS = 'league.forms.LeagueSignupForm'

# required by MAchina
CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
  },
  'machina_attachments': {
    'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    'LOCATION': '/tmp',
  }
}

HAYSTACK_CONNECTIONS = {
  'default': {
    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
  },
}

MACHINA_BASE_TEMPLATE_NAME = 'full_width.html'
MACHINA_MARKUP_LANGUAGE = ('openstudyroom.mistune.osr_markdown', {'safe_mode': True})
MACHINA_MARKUP_WIDGET = 'openstudyroom.widget.MarkdownTextareaWidget'
MACHINA_FORUM_NAME = 'OSR Forums'


#Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
#CSRF_COOKIE_SECURE = True
#CSRF_COOKIE_HTTPONLY = True
#SESSION_COOKIE_SECURE = True

CRON_CLASSES = [
    'league.cron.ScraperCronJob',
]

INTERNAL_IPS = ['127.0.0.1']

POSTMAN_AUTO_MODERATE_AS = True

WAGTAILIMAGES_MAX_UPLOAD_SIZE = 20 * 1024 * 1024



# Default settings
BOOTSTRAP3 = {

    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    #'base_url': '/static/bootstrap-3.3.7/dist/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    #'css_url': '/static/bootstrap-3.3.7/dist/css/bootstrap.min.css',
    'css_url': '/static/css/bootstrap.min.css',

    # The complete URL to the Bootstrap CSS file (None means no theme)
    #'theme_url': '/static/bootstrap-3.3.7/dist/css/bootstrap-theme.min.css',
    #'theme_url': '/static/css/bootstrap-theme.min.css',

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,
}
