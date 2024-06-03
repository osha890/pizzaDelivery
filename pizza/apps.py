from django.apps import AppConfig


class PizzaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pizza'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
