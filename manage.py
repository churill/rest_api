#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

env = environ.Env()
READ_ENV_FILE = env.bool('DJANGO_SETTINGS_READ_ENV_FILE', default=False)
if READ_ENV_FILE:
    env.read_env('.env')

debug = env.bool('DEBUG', False)


def main():
    """Run administrative tasks."""
    if debug:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.local')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
