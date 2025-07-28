import json
from uuid import UUID

from dotenv import dotenv_values
from fastapi import HTTPException
from kafka import KafkaConsumer, KafkaProducer

from api.kafka import KafkaClientFactory
from api.service import RecommendationService
from api.utils import logger

class KafkaRecommendationService:
	__consumer: KafkaConsumer | None = KafkaClientFactory.get_consumer()
	__producer: KafkaProducer | None = KafkaClientFactory.get_producer()
	__recommendation_service: RecommendationService = None

	__env = dotenv_values()

	def __init__(self, recommendation_service: RecommendationService):
		self.__recommendation_service = recommendation_service

	@staticmethod
	def __parse_uuid(string: str) -> UUID:
		user_uuid_str = json.loads(string)

		return UUID(user_uuid_str)

	@staticmethod
	def __prepare_response(ids: list[UUID]) -> str:
		return json.dumps([str(uid) for uid in ids])

	def consume(self):
		error_topic = self.__env['KAFKA_ERROR_TOPIC']

		if self.__consumer is None or self.__producer is None:
			logger.error('consume[1]: KafkaConsumer or KafkaProducer is None')
			return

		while True:
			try:
				records = self.__consumer.poll(timeout_ms=5000)

				for partition, messages in records.items():
					for message in messages:
						try:
							logger.info(f"consume[2]: partition is {partition}, message is {message}")
							logger.debug(f'consume[3]: message_id is {message.key}')

							self.__handle_message(message)

						except HTTPException as e:
							logger.error(f'consume[5]: {e}')

							error_data = {
								"error_type": "HTTPException",
								"status_code": e.status_code,
								"detail": e.detail
							}

							serialized_error_data = json.dumps(error_data)

							self.__producer.send(
								topic=error_topic,
								key=message.key,
								value=serialized_error_data,
								headers=[
									('origin_topic', partition.topic.encode()),
									('kafka_correlationId', message.key)
								]
							)
			except Exception as e:
				logger.critical(f'consume[6]: {e}')

	def __handle_message(self, message):
		if self.__producer is None:
			logger.error('consume[7]: KafkaProducer is None')
			return

		producer_topic = self.__env['KAFKA_RESPONSE_TOPIC']

		if message.key is None:
			raise HTTPException(detail='invalid key', status_code = 400)

		message_id = message.key
		user_uuid = self.__parse_uuid(message.value)

		response = self.__recommendation_service.find_potential_friends(user_uuid)
		payload = self.__prepare_response(response)

		logger.debug(f'consume[4]: response is {response}')

		self.__producer.send(
			topic=producer_topic,
			key=message_id,
			value=payload,
			headers=[('kafka_correlationId', message_id)]
		)