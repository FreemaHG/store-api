import random
from http import HTTPStatus

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.routes.base import BaseAPIRouter
from src.schemas.product import ProductSchema
from src.schemas.response import ResponseSchema
from src.services.product import ProductService
from src.utils.exceptions import CustomApiException


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
    Возврат товаров
    """
    products_list = await ProductService.get_list(session=session)
    random.shuffle(products_list)  # Перемешиваем товары

    return products_list


@router.get(
    '/products/{product_id}/',
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
        raise CustomApiException(status_code=HTTPStatus.NOT_FOUND, detail='Товар не найден')

    return post