from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from .models import create_default_site, create_default_superuser
        post_migrate.connect(create_default_site, sender=self)
        post_migrate.connect(create_default_superuser, sender=self)