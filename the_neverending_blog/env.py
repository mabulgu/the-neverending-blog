import os

from django.core.exceptions import ImproperlyConfigured

environment = os.getenv("APP_ENV")

if environment is None:
    raise ImproperlyConfigured("The APP_ENV environment must not be empty.")


def set_default_env():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_neverending_blog.settings.{env}'.format(env=environment))