from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.posts.schemas.category import CategorySchema
from src.posts.services.category import CategoryService


router = APIRouter(tags=['Категории'])

@router.get(
    '/categories/',
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
