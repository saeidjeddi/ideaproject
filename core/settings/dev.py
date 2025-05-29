from .base import *



SECRET_KEY = 'django-insecure-2oluxsxklsc_0(%b*w9#rwmm51a52w$+55fvf1#4u1kglt!)1-'

DEBUG = True

ALLOWED_HOSTS = ["https://saeidjeddi.ir", "http://saeidjeddi.ir", "saeeidjeddi.ir", "www.saeidjeddi.ir", "*"]

CSRF_TRUSTED_ORIGINS = ["https://saeidjeddi.ir",]


INSTALLED_APPS +=[
    'rest_framework',
    'rest_framework_simplejwt',



    'home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'idea',
        'USER': 'root',
        'PASSWORD': 'S@eed#9776',
        'HOST': '141.98.210.124',
        'PORT': '3306',
    }
}




STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.parent / '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / '/media/'




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
                            'accounts.authentication.EmailAuthBackend',
                            'accounts.authentication.UserAuthBackend',
                            ]
