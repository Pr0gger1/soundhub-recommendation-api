from typing import Optional
from uuid import UUID

from fastapi import Depends

from api.utils.di import DependencyInjector as di
from api.service import RecommendationService
from api.utils import logger
from app import router

@router.get("/recommend/{user_id}")
async def recommend_users(
    user_id: UUID,
    service: Optional[RecommendationService] = Depends(di.get_recommend_service)
):
    logger.debug(f"recommend_users[1]: user_id = {user_id}")
    friend_list = service.find_potential_friends(user_id)

    logger.info(f'recommend_users[2]: {friend_list}')

    return friend_list
