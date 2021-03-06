# Django settings for protocoller project.
import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

ADMINS = (
     ('Dmitry Sukhov', 'dmitry.sukhov@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(SITE_ROOT, 'db', 'main'),
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

DATE_FORMAT = 'N j, Y'


STATIC_ROOT = '/home/quoter/www/'
STATIC_URL = '/static/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ta^4n6q(n50s7%)^nx-3u^i@l+owel-veww#!&8yf_r7bsd((g'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
  #  'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'openid_consumer.middleware.OpenIDMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)


OPENID_CREATE_USERS = True
OPENID_UPDATE_DETAILS_FROM_SREG = True

ROOT_URLCONF = 'protocoller.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'template'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'protocoller.miner',
    'django.contrib.admin',
    'pytils',
    'django.contrib.markup',
    'south',
    'socialauth',
    'openid_consumer',
    'registration',
    'markitup',
    'debug_toolbar',
    'perfect404',
    'indexer',
    'paging',
    'sentry',
    'raven.contrib.django',
    'sorl.thumbnail',
    'crispy_forms',
    'dajaxice',
    'dajax'
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
OPENID_REDIRECT_NEXT = '/accounts/openid/done/'
LOGIN_URL = "/login/"

OPENID_SREG = {"requred": "nickname, email, fullname",
               "optional": "postcode, country",
               "policy_url": ""}

#example should be something more like the real thing, i think
OPENID_AX = [{"type_uri": "http://axschema.org/contact/email",
              "count": 1,
              "required": True,
              "alias": "email"},
             {"type_uri": "http://axschema.org/schema/fullname",
              "count": 1,
              "required": False,
              "alias": "fname"}]

OPENID_AX_PROVIDER_MAP = {'Google': {'email': 'http://axschema.org/contact/email',
                                     'firstname': 'http://axschema.org/namePerson/first',
                                     'lastname': 'http://axschema.org/namePerson/last'},
                          'Default': {'email': 'http://axschema.org/contact/email',
                                      'fullname': 'http://axschema.org/namePerson',
                                      'nickname': 'http://axschema.org/namePerson/friendly'}
                          }

TWITTER_CONSUMER_KEY = 'Nqm35m6800IKFYBhrnJocQ'
TWITTER_CONSUMER_SECRET = 'pTuRoC2lf1IBC80q4YIh0ZqTdTJNMe1o1nw7jMbQxA'
TWITTER_REQUEST_TOKEN_URL = 'http://twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'http://twitter.com/oauth/access_token'
TWITTER_AUTHORIZATION_URL = 'http://twitter.com/oauth/authorize'


FACEBOOK_APP_ID = '171106619588637'
FACEBOOK_API_KEY = 'c002be0240ddd8903c21d59dcfc8f42e'
FACEBOOK_SECRET_KEY = '575540f1d0b8ec62f39815a4e3b8761a'

LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'socialauth.auth_backends.OpenIdBackend',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "socialauth.context_processors.facebook_api_key",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "protocoller.miner.context_processors.maps_api_key",
    "protocoller.miner.context_processors.compare_list",
    "django.core.context_processors.static"
    )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

#django-registration settings
ACCOUNT_ACTIVATION_DAYS = 10

#Yandex maps API key
YANDEX_MAPS_API_KEY = 'AODzFE0BAAAAoXcZYwIAG1u61AXDPbZD7AdmjO1-aSAjBZoAAAAAAAAAAABTlA6cYksJKJo4ORU9l6EgMBk7TQ=='

#django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)

#MAPS API
MAPS_API_KEY = "AODzFE0BAAAAoXcZYwIAG1u61AXDPbZD7AdmjO1-aSAjBZoAAAAAAAAAAABTlA6cYksJKJo4ORU9l6EgMBk7TQ=="

SITE_ID = 2

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'miner_cache_table',
    }
}

CACHE_BACKEND = 'db://miner_cache_table'

CRISPY_TEMPLATE_PACK = 'bootstrap'
