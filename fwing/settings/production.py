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
