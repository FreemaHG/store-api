from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.schemas.category import CategorySchema
from src.products.services.category import CategoryService
from src.router import BaseRouter


router = BaseRouter(tags=['Категории'])

@router.get(
    '/categories',
    name="Возврат категорий",
    description="Возврат категорий",
    response_model=list[CategorySchema],
    responses={
        200: {'model': list[CategorySchema]}
    },
)
async def get_categories(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Возврат категорий
    """
    dishes_list = await CategoryService.get_categories(session=session)

    return dishes_list
