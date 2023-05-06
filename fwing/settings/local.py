from fwing.settings.base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_DEV_ENGINE"),
        "NAME": os.environ.get("DB_DEV_NAME"),
        "USER": os.environ.get("DB_DEV_USER"),
        "PASSWORD": os.environ.get("DB_DEV_PASSWORD"),
        "HOST": os.environ.get("DB_DEV_HOST"),
        "PORT": os.environ.get("DB_DEV_PORT"),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
