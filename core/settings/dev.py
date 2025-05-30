from .base import *



SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ["https://saeidjeddi.ir", "http://saeidjeddi.ir", "saeeidjeddi.ir", "www.saeidjeddi.ir", "*"]

CSRF_TRUSTED_ORIGINS = ["https://saeidjeddi.ir",]


INSTALLED_APPS +=[
    'rest_framework',
    'rest_framework_simplejwt',
    # 'oauth2_provider',



    'home.apps.HomeConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.blog.apps.BlogConfig',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('Name_DB'),
        'USER': config('User_DB'),
        'PASSWORD': config('Password_DB'),
        'HOST': config('HOST_DB'),
        'PORT': '3306',
    }
}




STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/ideaproject/static'

# STATIC_ROOT = BASE_DIR.parent / 'static/'
#
# STATICFILES_DIRS = [
#     BASE_DIR.parent / 'static/',
# ]



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'media/'




REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}




WSGI_APPLICATION  = "core.wsgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           'apps.accounts.authentication.EmailAuthBackend',
                           'apps.accounts.authentication.UserAuthBackend',
                            ]



SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_AGE = 86400





REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
