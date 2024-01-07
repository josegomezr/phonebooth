from .settings import *

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname:10s} {asctime} {name:20} [p:{process:x}|{thread:x}]\n{message}\n",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "verbose"
        },
        "console-sql": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": 'INFO',
        },
        'django.db.backends': {
            "handlers": ["console-sql"],
            'level': 'INFO',
        },
        'calls': {
            "handlers": ["console"],
            'level': 'INFO',
        }
    },
}
