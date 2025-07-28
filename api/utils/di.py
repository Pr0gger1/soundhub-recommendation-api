from typing import Optional

from api.data.database import Database
from api.kafka.KafkaRecommendationService import KafkaRecommendationService
from api.repository import GenreRepository
from api.service import RecommendationService


class DependencyInjector:
    @staticmethod
    def get_recommend_service() -> Optional[RecommendationService]:
        return RecommendationService(
            DependencyInjector.get_user_repository()
        )

    @staticmethod
    def get_kafka_service() -> Optional[KafkaRecommendationService]:
        return KafkaRecommendationService(DependencyInjector.get_recommend_service())

    @staticmethod
    def get_db() -> Optional[Database]:
        return Database()

    @staticmethod
    def get_user_repository():
        return GenreRepository(db=DependencyInjector.get_db())