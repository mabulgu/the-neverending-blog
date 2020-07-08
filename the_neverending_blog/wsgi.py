"""
WSGI config for the_neverending_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.exceptions import ImproperlyConfigured
from django.core.wsgi import get_wsgi_application
from the_neverending_blog.env import set_default_env

set_default_env()

application = get_wsgi_application()
