from django.apps import AppConfig

class SearchbookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'searchbook'

    def ready(self):
        # Bu yerga importni joylaymiz — apps yuklangach ishlaydi
        try:
            import searchbook.run_once
        except Exception as e:
            print(f"run_once.py ishlashida xatolik: {e}")
