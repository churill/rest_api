"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import environ

env = environ.Env()
READ_ENV_FILE = env.bool('DJANGO_SETTINGS_READ_ENV_FILE', default=False)
if READ_ENV_FILE:
    env.read_env('.env')

debug = env.bool('DEBUG', False)
if debug:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.production')

application = get_wsgi_application()
