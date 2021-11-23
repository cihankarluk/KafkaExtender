import logging
from typing import List

__all__ = ["CustomKafkaConsumer"]

from kafka import KafkaConsumer, OffsetAndMetadata
from kafka.consumer.fetcher import ConsumerRecord
from simple_settings import settings

logger = logging.getLogger(__name__)


class CustomKafkaConsumer:
    def __init__(self, topic: str, enable_auto_commit: bool = False):
        self.topics: list = [topic]
        self.group_id = settings.KAFKA_GROUP_ID
        self.max_records = settings.KAFKA_MAX_RECORDS
        self.timeout_ms = settings.KAFKA_TIMEOUT_MS
        self.enable_auto_commit = enable_auto_commit
        self.consumer: KafkaConsumer = None

    def __get_config(self):
        config = {
            "bootstrap_servers": settings.KAFKA_HOST,
            "api_version": (2, 8, 1),
            "value_deserializer": lambda v: v.decode(),
            "auto_offset_reset": "earliest",
            "group_id": self.group_id,
            "enable_auto_commit": self.enable_auto_commit,
        }
        return config

    def __get_connection(self):
        kafka_conf = self.__get_config()
        logger.info(f"Kafka consumer config: '{kafka_conf}'")
        self.consumer = KafkaConsumer(*self.topics, **kafka_conf)

    def __ensure_connection(self):
        if not self.consumer:
            self.__get_connection()

    def consumer_commit(self, partition, offset):
        self.consumer.commit({partition: OffsetAndMetadata(offset, None)})

    def read_single_message_with_commit(self) -> List[ConsumerRecord]:
        self.__ensure_connection()
        message = []

        partitions = self.consumer.poll(timeout_ms=self.timeout_ms, max_records=1)
        for partition in partitions:
            message = partitions[partition]

            if not self.enable_auto_commit:
                self.consumer_commit(partition=partition, offset=message[-1].offset + 1)

        self.consumer.unsubscribe()
        self.consumer.close()
        return message

    def read_all_messages_without_commit(self) -> List[ConsumerRecord]:
        self.__ensure_connection()
        messages = []

        partitions = self.consumer.poll(self.timeout_ms, self.max_records)
        while partitions:
            for partition in partitions:
                messages.extend(partitions[partition])

            partitions = self.consumer.poll(self.timeout_ms, self.max_records)

        self.consumer.unsubscribe()
        self.consumer.close(autocommit=False)
        return messages

    def close_without_commit(self):
        self.consumer.close(autocommit=False)
