import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-votre-cle-secrete-ici')

# API Key
POSITIONSTACK_API_KEY = os.environ.get('POSITIONSTACK_API_KEY', '88bcabc4997f720becd5cb84b44c7b6e')

# Mode DEBUG
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hosts autorisés
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Applications tierces
    'crispy_forms',
    'crispy_bootstrap5',
    'rest_framework',
    'corsheaders',
    'whitenoise.runserver_nostatic',
    # Vos applications
    'gestion',
    'gestion.geolocalisation',
    'chauffeurs_mobile',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'transport_app.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'transport_app.wsgi.application'

# Base de données
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
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

# Internationalization
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Fichiers statiques avec WhiteNoise
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Prix des courses selon le type de chauffeur
PRIX_COURSE_TAXI = 15.0
PRIX_COURSE_CHAUFFEUR = 10.0
PRIX_COURSE_SOCIETE = 0.0

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Configuration pour Folium (carte)
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (35.8256, 10.6415),
    'DEFAULT_ZOOM': 12,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'RESET_VIEW': False,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'Systeme de Gestion Transport',
}

# Configuration Nominatim (géocodage)
NOMINATIM_USER_AGENT = 'gestion_transport_app'
NOMINATIM_TIMEOUT = 10

# Configuration CSP - adaptée pour Render
if not DEBUG:
    CSP_DEFAULT_SRC = ("'self'",)
    CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net", "https://unpkg.com")
    CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'", "https://cdn.jsdelivr.net", "https://unpkg.com")
    CSP_IMG_SRC = ("'self'", "data:", "https://*.tile.openstreetmap.org")
    CSP_FONT_SRC = ("'self'", "https://cdn.jsdelivr.net")
    CSP_CONNECT_SRC = ("'self'",)
    CSP_FRAME_ANCESTORS = ("'self'",)

# Configuration cache pour le géocodage
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

CACHE_GEOCODING = True
CACHE_TIMEOUT_GEOCODING = 86400

# Configuration OSRM pour le routage
OSRM_BASE_URL = 'http://router.project-osrm.org'

# Configuration de l'application géolocalisation
GEOCODING_SERVICES = ['positionstack', 'nominatim', 'fallback']
MAX_GEOCODING_RETRIES = 3
GEOCODING_TIMEOUT = 5

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'geolocation.log',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'gestion.geolocalisation': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': False,
        },
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Configuration CORS - adaptée pour Render
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:8080",
    ]
else:
    CORS_ALLOWED_ORIGINS = [
        "https://*.onrender.com",
    ]
    CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT']
CORS_ALLOW_HEADERS = ['accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with']

# Configuration des sessions
SESSION_COOKIE_NAME = 'sessionid_mobile'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 7 jours
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SAVE_EVERY_REQUEST = True
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = not DEBUG  # True en production (HTTPS)
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

# Cookies CSRF pour API
CSRF_COOKIE_NAME = 'csrftoken_mobile'
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = True

if DEBUG:
    CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000']
else:
    CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']
    
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SAMESITE = 'Lax'

# Sécurité supplémentaire en production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'