from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'


    # Import module signals when AppConfig is ready
    def ready(self):
        import accounts.signals

