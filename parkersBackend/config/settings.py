"""
Django settings for the Bris Parker project.

Generated using Django 4.2.
"""

from pathlib import Path


# Base directory of the Django project
BASE_DIR = Path(__file__).resolve().parent.parent


# Development settings
# Do not use these settings directly in production.

SECRET_KEY = (
    "django-insecure-"
    "cdchk8)8onhm^=w6t8q5#ey3wu#^h)#+c$+b7k5j@s#exany8s"
)

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# Installed applications

INSTALLED_APPS = [
    # Django applications
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Bris Parker applications
    "park_finder",
]


# Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# URL configuration

ROOT_URLCONF = "config.urls"


# Template configuration

TEMPLATES = [
    {
        "BACKEND": (
            "django.template.backends.django."
            "DjangoTemplates"
        ),
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                (
                    "django.template.context_processors."
                    "debug"
                ),
                (
                    "django.template.context_processors."
                    "request"
                ),
                (
                    "django.contrib.auth."
                    "context_processors.auth"
                ),
                (
                    "django.contrib.messages."
                    "context_processors.messages"
                ),
            ],
        },
    },
]


# WSGI application

WSGI_APPLICATION = "config.wsgi.application"


# Database
#
# SQLite is retained temporarily for frontend development.
# The backend team can replace this with PostgreSQL and
# PostGIS configuration during database integration.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# Internationalisation

LANGUAGE_CODE = "en-au"

TIME_ZONE = "Australia/Brisbane"

USE_I18N = True

USE_TZ = True


# Static files
#
# Files inside:
# park_finder/static/park_finder/
# will be discovered automatically because
# django.contrib.staticfiles is installed.

STATIC_URL = "static/"


# Default primary key type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"