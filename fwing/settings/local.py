from fwing.settings.base import *
import os
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG_MODE")

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True
# Si CORS_ORIGIN_ALLOW_ALL es False
# Lista de origenes permitidos
# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:3000",
# ]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DB_DEV_ENGINE"),
        "NAME": config("DB_DEV_NAME"),
        "USER": config("DB_DEV_USER"),
        "PASSWORD": config("DB_DEV_PASSWORD"),
        "HOST": config("DB_DEV_HOST"),
        "PORT": config("DB_DEV_PORT"),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = "static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
