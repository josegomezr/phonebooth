from django.conf import settings as dj_settings

def settings(_):
    return {
        "settings": {k: getattr(dj_settings, k) for k in dj_settings.GLOBAL_EXPOSED_SETTINGS}
    }