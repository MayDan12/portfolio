from django.apps import AppConfig


class HiveManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hive_manager'

# Import module signals when AppConfig is ready
    def ready(self):
        import hive_manager.signals
