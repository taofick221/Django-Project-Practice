from django.apps import AppConfig


class AuthpermissionConfig(AppConfig):
    name = 'AuthPermission'

    def ready(self):
        import AuthPermission.signals
        
