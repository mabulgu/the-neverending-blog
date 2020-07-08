from the_neverending_blog.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'neverendingblog',
        'USER': 'bastian',
        'PASSWORD': 'balthazar',
        'HOST': 'postgresql',
        'PORT': '5432',
    }
}