"""Development settings."""

from .base import *

# Base
DEBUG = True

# Security
SECRET_KEY = 'PB3aGvTmCkzaLGRAxDc3aMayKTPTDd5usT8gw4pCmKOk5AlJjh12pTrnNgQyOHCH'
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# django-extensions
INSTALLED_APPS += ['django_extensions']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{ROOT_DIR}/todos.log',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': "DEBUG",
            'propagate': True,
        },
    },
}