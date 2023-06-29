from fwing.settings.base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG_MODE")  # Must be false

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
        "ENGINE": config("DB_PROD_ENGINE"),
        "NAME": config("DB_PROD_NAME"),
        "USER": config("DB_PROD_USER"),  # Not works for sqlite
        "PASSWORD": config("DB_PROD_PASSWORD"),  # Not works for sqlite
        "HOST": config("DB_PROD_HOST"),  # Not works for sqlite
        "PORT": config("DB_PROD_PORT"),  # Not works for sqlite
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = "static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
