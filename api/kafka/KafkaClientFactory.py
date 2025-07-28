import json

from dotenv import dotenv_values
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import NoBrokersAvailable

from api.utils import logger

class KafkaClientFactory:
	_env = dotenv_values()
	_consumer: KafkaConsumer | None = None
	_producer: KafkaProducer | None = None

	@classmethod
	def _get_bootstrap_server(cls) -> str:
		host = cls._env['KAFKA_HOST']
		port = cls._env['KAFKA_PORT']

		return f'{host}:{port}'

	@classmethod
	def get_producer(cls) -> KafkaProducer | None:
		try:
			if cls._producer is None:
				cls._producer = KafkaProducer(
					bootstrap_servers=cls._get_bootstrap_server(),
					value_serializer=lambda x: json.dumps(x).encode('utf-8'),
				)
		except NoBrokersAvailable as e:
			logger.error(f'KafkaClientFactory[1]: {e}')
			return None

		return cls._producer

	@classmethod
	def get_consumer(cls) -> KafkaConsumer | None:
		topic = cls._env['KAFKA_REQUEST_TOPIC']

		try:
			if cls._consumer is None:
				cls._consumer = KafkaConsumer(
					topic,
					bootstrap_servers=cls._get_bootstrap_server(),
					value_deserializer=lambda x: x.decode('utf-8'),
					group_id=cls._env['KAFKA_CONSUMER_GROUP']
				)
		except NoBrokersAvailable as e:
			logger.error(f'KafkaClientFactory[2]: {e}')
			return None

		return cls._consumer