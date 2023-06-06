from django.apps import AppConfig


class TodoAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo_app"

    def ready(self):
        import todo_app.signal_receivers
