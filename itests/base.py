import json
import logging
import os
import unittest
from datetime import datetime

import pytz
from kafka import KafkaAdminClient
from kafka.errors import UnknownTopicOrPartitionError
from simple_settings import settings

from app.kafka.producer import CustomKafkaProducer

logger = logging.getLogger(__name__)


class BaseIntegrationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test_topic_1 = "test_topic_1"  # messages is going to be cleaned
        self.test_topic_2 = "test_topic_2"  # messages is going to be remain

    def tearDown(self) -> None:
        self.flush_kafka()

    @classmethod
    def setUpClass(cls) -> None:
        cls.flush_kafka()

    @classmethod
    def flush_kafka(cls):
        kafka_host = settings.KAFKA_HOST
        if settings.DEBUG and ("localhost" in kafka_host or "kafka" in kafka_host):
            return cls.__flush_kafka_data()

    @classmethod
    def __flush_kafka_data(cls):
        kafka_settings = {
            "bootstrap_servers": settings.KAFKA_HOST,
            "api_version": (2, 8, 1),
        }
        kac = KafkaAdminClient(**kafka_settings)

        try:
            kac.delete_topics(topics=["test_topic_1"])
        except UnknownTopicOrPartitionError:
            pass

    @staticmethod
    def read_file(filename: str):
        file_path = os.path.join(settings.ITEST_DIR, "datasets", filename)
        with open(file_path, "r") as file:
            data = file.read()
        return data

    @staticmethod
    def current_time():
        """
        :return: python datetime object for current time in utc timezone, this method adds tzinfo standart dt.dt.now()
        """
        return datetime.now(tz=pytz.utc)

    @classmethod
    def write_kafka_data(cls, count: int = 100, topic: str = "test_topic_1"):
        ckp = CustomKafkaProducer()
        for index in range(count):
            data = {"test": f"data_{index}"}
            ckp.publish(topic=topic, message=json.dumps(data), key=topic)

        ckp.publish(topic="test_topic_2", message="test_data")
        ckp.close()
