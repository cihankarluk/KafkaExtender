import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from app.kafka.consumer import CustomKafkaConsumer
from itests.base import BaseIntegrationTestCase


class CustomKafkaConsumerTestCase(BaseIntegrationTestCase):
    def setUp(self) -> None:
        super(CustomKafkaConsumerTestCase, self).setUp()

    def test__read_single_message_with_commit(self):
        self.write_kafka_data(topic=self.test_topic_1)

        ckc = CustomKafkaConsumer(topic=self.test_topic_1)
        message: List[ConsumerRecord] = ckc.read_single_message_with_commit()

        expected_record = {"test": "data_0"}
        record = json.loads(message[0].value)
        self.assertDictEqual(expected_record, record)

        ckc = CustomKafkaConsumer(topic=self.test_topic_1)
        message: List[ConsumerRecord] = ckc.read_single_message_with_commit()

        expected_record = {"test": "data_1"}
        record = json.loads(message[0].value)
        self.assertDictEqual(expected_record, record)

    def test__read_all_messages_without_commit(self):
        self.write_kafka_data(count=50, topic=self.test_topic_1)

        ckc = CustomKafkaConsumer(topic=self.test_topic_1)
        messages = ckc.read_all_messages_without_commit()

        self.assertEqual(50, len(messages))

        ckc = CustomKafkaConsumer(topic=self.test_topic_1)
        message: List[ConsumerRecord] = ckc.read_single_message_with_commit()

        expected_record = {"test": "data_0"}
        record = json.loads(message[0].value)

        self.assertDictEqual(expected_record, record)
        self.assertEqual(messages[0].value, message[0].value)
