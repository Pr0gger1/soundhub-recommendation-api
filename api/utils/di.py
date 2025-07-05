from typing import Optional

from api.data.database import Database
from api.repository import GenreRepository
from api.services import RecommendationService


class DependencyInjector:
    @staticmethod
    def get_recommend_service() -> Optional[RecommendationService]:
        return RecommendationService(
            genre_repository=DependencyInjector.get_user_repository()
        )

    @staticmethod
    def get_db() -> Optional[Database]:
        return Database()

    @staticmethod
    def get_user_repository():
        return GenreRepository(db=DependencyInjector.get_db())