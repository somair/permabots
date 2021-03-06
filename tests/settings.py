# flake8: noqa
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path helper
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)
DEBUG=True
USE_TZ=True
DATABASES={
           "default": {
                "ENGINE": "django.db.backends.sqlite3",
                }
           }
ROOT_URLCONF="tests.urls"
INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "permabots",
            "rest_framework",
            'rest_framework.authtoken',
            "tests"
        ]
SITE_ID=1
MIDDLEWARE_CLASSES=()

SECRET_KEY = "shds8dfyhskdfhskdfhskdf"

STATIC_URL = '/static/'
STATIC_ROOT = location('/static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
CELERY_ALWAYS_EAGER = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s '
#                       '%(process)d %(thread)d %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#     },
#     'loggers': {
#         'permabots': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     }
# }