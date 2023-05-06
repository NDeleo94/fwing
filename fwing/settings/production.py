from fwing.settings.base import *
from ast import literal_eval
import os

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = literal_eval(os.environ.get("DEBUG_MODE"))
DEBUG = True  # Must be false

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_PROD_ENGINE"),
        "NAME": os.environ.get("DB_PROD_NAME"),
        "USER": os.environ.get("DB_PROD_USER"),  # Not works for sqlite
        "PASSWORD": os.environ.get("DB_PROD_PASSWORD"),  # Not works for sqlite
        "HOST": os.environ.get("DB_PROD_HOST"),  # Not works for sqlite
        "PORT": os.environ.get("DB_PROD_PORT"),  # Not works for sqlite
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
