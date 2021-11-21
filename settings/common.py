import os

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)s %(message)s"},  # noqa
    },
    "handlers": {
        "log_to_stdout": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
}


KAFKA_HOST = os.environ.get("KAFKA_HOST", "localhost:29092")
KAFKA_GROUP_ID = os.environ.get("KAFKA_GROUP_ID", "test_group")
KAFKA_MAX_RECORDS = int(os.environ.get("KAFKA_MAX_RECORDS", 500))
KAFKA_TIMEOUT_MS = int(os.environ.get("KAFKA_TIMEOUT_MS", 30))

SETTINGS_IMPORTED = True
