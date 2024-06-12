from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.routes.base import BaseAPIRouter
from src.schemas.category import CategorySchema
from src.services.category import CategoryService


router = BaseAPIRouter(tags=['category'])

@router.get(
    '/categories',
    response_model=list[CategorySchema],
    responses={
        200: {'model': list[CategorySchema]}
    },
)
async def get_categories(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Вывод категорий
    """
    dishes_list = await CategoryService.get_categories(session=session)

    return dishes_list
