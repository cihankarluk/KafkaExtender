import json

from app.kafka.producer import CustomKafkaProducer
from itests.base import BaseIntegrationTestCase


class CustomKafkaProducerTestCase(BaseIntegrationTestCase):
    def setUp(self):
        self.ckp = CustomKafkaProducer()

    def test__publish(self):
        data = {"test": "data"}
        self.ckp.publish("test_topic", json.dumps(data))

    def test__publish__multiple_topics(self):
        data_1 = {"test": "data"}
        data_2 = {"test": "data_2"}
        data_3 = {"test": "data_3"}

        self.ckp.publish(topic="test_topic_1", message=json.dumps(data_1))
        self.ckp.publish(topic="test_topic_2", message=json.dumps(data_2))
        self.ckp.publish(topic="test_topic_1", message=json.dumps(data_3))
        self.ckp.publish(topic="test_topic_2", message=json.dumps(data_3))

        self.ckp.close()
