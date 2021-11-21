# Kafka Extender

It is helper service for extend python-kafka implementation.



tox compatible python versions:

```
3.8.9
```

## Environment Variables

- SIMPLE_SETTINGS (required)
- DEBUG (default=False)

- KAFKA_HOST (required)
- KAFKA_GROUP_ID (default="")
- KAFKA_TIMEOUT_MS (default=30)
- KAFKA_MAX_RECORDS (default=500)

## Installing Dependencies

```
$ pip install .
```

## Local Development

```
$ export SIMPLE_SETTINGS=tests.settings
```

## Deploy and Running Integrations Tests on Local

```
$ docker-compose -f itests/docker-compose.yml build
$ docker-compose -f itests/docker-compose.yml up


$ docker exec -it kafka-app pytest itests
```

# Some Kafka Codes

List Topics:
```shell
$ docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --list
```

Delete Topic:
```shell
$ docker exec -it kafka kafka-topics.sh --delete --topic <topic_name>
```

List Topic Messages:
```shell
$ docker exec -it kafka kafka-console-consumer.sh --from-beginning --bootstrap-server localhost:9092  --topic <topic_name>
```
