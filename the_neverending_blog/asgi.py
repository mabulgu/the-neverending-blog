"""
ASGI config for the_neverending_blog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from the_neverending_blog.env import set_default_env

set_default_env()

application = get_asgi_application()
