"""Development settings."""

from .base import *
from .base import env
from datetime import timedelta

# Base
DEBUG = True

TEST_RUNNER = "django.test.runner.DiscoverRunner"

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

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}