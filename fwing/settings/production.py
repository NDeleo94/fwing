from fwing.settings.base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG_MODE")

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
