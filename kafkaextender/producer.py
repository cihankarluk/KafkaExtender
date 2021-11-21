import logging

__all__ = ["CustomKafkaProducer"]

from kafka import KafkaProducer
from simple_settings import settings

logger = logging.getLogger(__name__)


class CustomKafkaProducer:
    def __init__(self):
        self.producer: KafkaProducer = None

    @staticmethod
    def __get_conf() -> dict:
        config = {
            "bootstrap_servers": settings.KAFKA_HOST,
            "compression_type": "lz4",
            "api_version": (2, 8, 1),
            "key_serializer": lambda k: k.encode("utf-8") if k else None,
            "value_serializer": lambda v: v.encode("utf-8"),
            "retries": 3,
        }
        return config

    def __get_connection(self):
        kafka_conf = self.__get_conf()
        logger.info(f"Kafka producer config: '{kafka_conf}'")
        self.producer = KafkaProducer(**kafka_conf)

    def __ensure_connection(self):
        if not self.producer:
            self.__get_connection()

    def publish(self, topic, message, key=None):
        self.__ensure_connection()
        self.producer.send(topic, value=message, key=key)

    def batch(self, topic, messages):
        self.__ensure_connection()
        for value in messages:
            self.producer.send(topic, value)
        self.producer.flush()

    def batch_keyed(self, topic, messages: dict):
        self.__ensure_connection()
        for key, value in messages.items():
            self.producer.send(topic, value=value, key=key)
        self.producer.flush()

    def flush(self):
        if self.producer:
            self.producer.flush()

    def close(self):
        if self.producer:
            self.producer.flush()
            self.producer.close()
