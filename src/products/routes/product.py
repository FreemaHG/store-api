import random

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.database import get_async_session
from src.products.schemas.product import ProductSchema
from src.router import BaseRouter
from src.schemas import ResponseSchema
from src.products.services.product import ProductService


router = BaseRouter(tags=['Товары'])

@router.get(
    '/products/',
    name="Возврат товаров",
    description="Возврат всех товаров",
    response_model=list[ProductSchema],
    responses={
        200: {'model': list[ProductSchema]}
    },
)
async def get_products(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Возврат товаров
    """
    products_list = await ProductService.get_list(session=session)
    random.shuffle(products_list)  # Перемешиваем товары

    return products_list


@router.get(
    '/products/{product_id}/',
    name="Возврат товара",
    description="Возврат товара по id",
    response_model=ProductSchema,
    responses={
        200: {'model': ProductSchema},
        404: {'model': ResponseSchema},
    }
)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Возврат товара
    """
    post = await ProductService.get(product_id=product_id, session=session)

    if not post:
        raise HTTPException(status_code=status.NOT_FOUND, detail='Товар не найден')

    return post