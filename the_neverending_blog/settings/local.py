from the_neverending_blog.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neverendingblog',
        'USER': 'bastian',
        'PASSWORD': 'balthazar',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}