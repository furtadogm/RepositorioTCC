import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]  # mesma coisa de .parent.parent.parent

SECRET_KEY = os.getenv("SECRET_KEY") or exec('raise AttributeError("SECRET_KEY")')

# SECURITY WARNING: don't run with debug turned on in production!

if os.getenv("DEBUG") not in ["True", "False"]:
    raise AttributeError("DEBUG on .env must be True or False")

DEBUG = os.getenv("DEBUG") == "True"


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"
