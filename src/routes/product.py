import random

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.routes.base import BaseAPIRouter
from src.schemas.product import ProductSchema
from src.services.product import ProductService

router = BaseAPIRouter(tags=['Товары'])

@router.get(
    '/products',
    response_model=list[ProductSchema],
    responses={
        200: {'model': list[ProductSchema]}
    },
)
async def get_products(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Вывод товаров
    """
    products_list = await ProductService.get_products(session=session)
    random.shuffle(products_list)  # Перемешиваем товары

    return products_list
