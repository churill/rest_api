"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import environ

env = environ.Env(DEBUG=(bool, False))
env.read_env(os.path.join(os.getcwd(), '.env'))
if env('DEBUG'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.production')

application = get_wsgi_application()
