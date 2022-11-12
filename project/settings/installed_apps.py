# Application definition

DJANGO_BUILT_IN_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "imagekit",  # pip install django-imagekit
    "crispy_forms",  # pip install django-crispy-forms
]

PROJECT_APPS = [
    "apps.core",
]

INSTALLED_APPS = DJANGO_BUILT_IN_APPS + THIRD_PARTY_APPS + PROJECT_APPS
