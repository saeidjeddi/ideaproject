from .base import *



SECRET_KEY = 'django-insecure-2oluxsxklsc_0(%b*w9#rwmm51a52w$+55fvf1#4u1kglt!)1-'

DEBUG = False

ALLOWED_HOSTS = ["https://saeidjeddi.ir", "http://saeidjeddi.ir", "saeeidjeddi.ir", "www.saeidjeddi.ir", "*"]

CSRF_TRUSTED_ORIGINS = ["https://saeidjeddi.ir",]


INSTALLED_APPS +=[
    'home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'idea',
        'USER': 'postgres',
        'PASSWORD': 'S@eed#9776',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}




STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.parent / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'media'




REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )

}




AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                            'accounts.authentication.EmailAuthBackend',
                            'accounts.authentication.UserAuthBackend',
                            ]
