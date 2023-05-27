from fwing.settings.base import *
from ast import literal_eval
import os

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = literal_eval(os.environ.get("DEBUG_MODE"))
DEBUG = True  # Must be false

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
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ndeleo94$default",
        "USER": "ndeleo94",  # Not works for sqlite
        "PASSWORD": "adminadmin",  # Not works for sqlite
        "HOST": "ndeleo94.mysql.pythonanywhere-services.com",  # Not works for sqlite
        "PORT": "3306",  # Not works for sqlite
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = "static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
