"""
Django settings for boofilsic project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nbv58c^&b8-095(^)&_BV98596v)&CX#^$&%*^V5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# To allow debug in template context
# https://docs.djangoproject.com/en/3.1/ref/settings/#internal-ips
INTERNAL_IPS = [
    "127.0.0.1"
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'hijack',
    'hijack.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.postgres',
    'django_sass',
    'django_rq',
    'simple_history',
    'markdownx',
    'management.apps.ManagementConfig',
    'mastodon.apps.MastodonConfig',
    'common.apps.CommonConfig',
    'users.apps.UsersConfig',
    'books.apps.BooksConfig',
    'movies.apps.MoviesConfig',
    'music.apps.MusicConfig',
    'games.apps.GamesConfig',
    'sync.apps.SyncConfig',
    'collection.apps.CollectionConfig',
    'timeline.apps.TimelineConfig',
    'easy_thumbnails',
    'user_messages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hijack.middleware.HijackUserMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'boofilsic.urls'

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
                # 'django.contrib.messages.context_processors.messages',
                "user_messages.context_processors.messages",
                'boofilsic.context_processors.site_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'boofilsic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'test'),
            'USER': os.environ.get('DB_USER', 'postgres'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'admin123'),
            'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
            'OPTIONS': {
                'client_encoding': 'UTF8',
                # 'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_DEFAULT,
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'boofilsic',
            'USER': 'doubaniux',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'OPTIONS': {
                'client_encoding': 'UTF8',
                # 'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_DEFAULT,
            }
        }
    }

# Customized auth backend, glue OAuth2 and Django User model together
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#authentication-backends

AUTHENTICATION_BACKENDS = [
    'mastodon.auth.OAuth2Backend',
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '{levelname} {asctime} {name}:{lineno} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'log'),
                'formatter': 'simple'
            },
        },
        'root': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

AUTH_USER_MODEL = 'users.User'

SILENCED_SYSTEM_CHECKS = [
    "auth.W004",  # User.username is non-unique
    "admin.E404"  # Required by django-user-messages
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))
SITE_INFO = {
    'site_name': 'NiceDB',
    'support_link': 'https://github.com/doubaniux/boofilsic/issues',
    'version_hash': None,
    'settings_module': os.getenv('DJANGO_SETTINGS_MODULE'),
    'sentry_dsn': None,
}

# Mastodon configs
CLIENT_NAME = os.environ.get('APP_NAME', 'NiceDB')
SITE_INFO['site_name'] = os.environ.get('APP_NAME', 'NiceDB')
APP_WEBSITE = os.environ.get('APP_URL', 'https://nicedb.org')
REDIRECT_URIS = APP_WEBSITE + "/users/OAuth2_login/"


# Path to save report related images, ends with slash
REPORT_MEDIA_PATH_ROOT = 'report/'
MARKDOWNX_MEDIA_PATH = 'review/'
BOOK_MEDIA_PATH_ROOT = 'book/'
DEFAULT_BOOK_IMAGE = os.path.join(BOOK_MEDIA_PATH_ROOT, 'default.svg')
MOVIE_MEDIA_PATH_ROOT = 'movie/'
DEFAULT_MOVIE_IMAGE = os.path.join(MOVIE_MEDIA_PATH_ROOT, 'default.svg')
SONG_MEDIA_PATH_ROOT = 'song/'
DEFAULT_SONG_IMAGE = os.path.join(SONG_MEDIA_PATH_ROOT, 'default.svg')
ALBUM_MEDIA_PATH_ROOT = 'album/'
DEFAULT_ALBUM_IMAGE = os.path.join(ALBUM_MEDIA_PATH_ROOT, 'default.svg')
GAME_MEDIA_PATH_ROOT = 'game/'
DEFAULT_GAME_IMAGE = os.path.join(GAME_MEDIA_PATH_ROOT, 'default.svg')
COLLECTION_MEDIA_PATH_ROOT = 'collection/'
DEFAULT_COLLECTION_IMAGE = os.path.join(COLLECTION_MEDIA_PATH_ROOT, 'default.svg')
SYNC_FILE_PATH_ROOT = 'sync/'
EXPORT_FILE_PATH_ROOT = 'export/'

# Allow user to login via any Mastodon/Pleroma sites
MASTODON_ALLOW_ANY_SITE = False

# Timeout of requests to Mastodon, in seconds
MASTODON_TIMEOUT = 30

MASTODON_CLIENT_SCOPE = 'read write follow'
# use the following if it's a new site
#MASTODON_CLIENT_SCOPE = 'read:accounts read:follows read:search read:blocks read:mutes write:statuses write:media'

MASTODON_LEGACY_CLIENT_SCOPE = 'read write follow'

# Tags for toots posted from this site
MASTODON_TAGS = '#NiceDB #NiceDB%(category)s #NiceDB%(category)s%(type)s'

# Emoji code in mastodon
STAR_SOLID = ':star_solid:'
STAR_HALF = ':star_half:'
STAR_EMPTY = ':star_empty:'

# Default password for each user. since password is not used any way,
# any string that is not empty is ok
DEFAULT_PASSWORD = 'ab7nsm8didusbaqPgq'

# Default redirect loaction when access login required view
LOGIN_URL = '/users/login/'

# Admin site root url
ADMIN_URL = 'tertqX7256n7ej8nbv5cwvsegdse6w7ne5rHd'

# Luminati proxy settings
LUMINATI_USERNAME = 'lum-customer-hl_nw4tbv78-zone-static'
LUMINATI_PASSWORD = 'nsb7te9bw0ney'

SCRAPING_TIMEOUT = 90

# ScraperAPI api key
SCRAPERAPI_KEY = '***REMOVED***'
PROXYCRAWL_KEY = None
SCRAPESTACK_KEY = None

# Spotify credentials
SPOTIFY_CREDENTIAL = "***REMOVED***"

# IMDb API service https://imdb-api.com/
IMDB_API_KEY = "***REMOVED***"

# The Movie Database (TMDB) API Keys
TMDB_API3_KEY = "***REMOVED***"
# TMDB_API4_KEY = "deadbeef.deadbeef.deadbeef"

# Google Books API Key
GOOGLE_API_KEY = '***REMOVED***'

# IGDB
IGDB_CLIENT_ID = 'deadbeef'
IGDB_CLIENT_SECRET = 'deadbeef'

# Thumbnail setting
# It is possible to optimize the image size even more: https://easy-thumbnails.readthedocs.io/en/latest/ref/optimize/
THUMBNAIL_ALIASES = {
    '': {
        'normal': {
            'size': (200, 200),
            'crop': 'scale',
            'autocrop': True,
        },
    },
}
# THUMBNAIL_PRESERVE_EXTENSIONS = ('svg',)
if DEBUG:
    THUMBNAIL_DEBUG = True

# https://django-debug-toolbar.readthedocs.io/en/latest/
# maybe benchmarking before deployment

REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')

RQ_QUEUES = {
    'mastodon': {
        'HOST': REDIS_HOST,
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': -1,
    },
    'export': {
        'HOST': REDIS_HOST,
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': -1,
    },
    'doufen': {
        'HOST': REDIS_HOST,
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': -1,
    }
}

RQ_SHOW_ADMIN_LINK = True

SEARCH_INDEX_NEW_ONLY = False


# SEARCH_BACKEND = 'MEILISEARCH'
# MEILISEARCH_SERVER = 'http://127.0.0.1:7700'
# MEILISEARCH_KEY = 'deadbeef'

SEARCH_BACKEND = 'TYPESENSE'
TYPESENSE_CONNECTION = {
    'api_key': 'xyz',
    'nodes': [{
        'host': 'localhost',
        'port': '8108',
        'protocol': 'http'
    }],
    'connection_timeout_seconds': 2
}

DOWNLOADER_RETRIES = 3
DOWNLOADER_SAVEDIR = None
ENABLE_NEW_MODEL = os.getenv('new_data_model')
if ENABLE_NEW_MODEL:
    INSTALLED_APPS.append('polymorphic')
    INSTALLED_APPS.append('catalog.apps.CatalogConfig')
    INSTALLED_APPS.append('journal.apps.JournalConfig')
    INSTALLED_APPS.append('social.apps.SocialConfig')
