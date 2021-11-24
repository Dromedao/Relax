from django.apps import AppConfig


class AppRelaxConfig(AppConfig):
    name = 'app_relax'

    def ready(self):
        import app_relax.signals
