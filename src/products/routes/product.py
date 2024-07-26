from typing import Optional, List

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.database import get_async_session
from src.products.repositories.product import ProductRepository
from src.products.schemas.product import ProductSchema
from src.router import BaseRouter
from src.schemas import ResponseSchema
from src.products.services.product import ProductService


router = BaseRouter(tags=['Товары'])

@router.get(
    '/products',
    name="Возврат товаров",
    description="Возврат товаров с возможностью фильтрации по id категории, названию, минимальной и максимальной цене товара",
    response_model=List[ProductSchema],
    responses={
        200: {'model': List[ProductSchema]}
    },
)
async def get_products(
    categoryId: Optional[int] = None,
    title: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
    limit: int = 100,
    offset: int = 0,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Возврат товаров
    """

    products = await ProductRepository.get_list(
        category_id=categoryId,
        title=title,
        price_min=price_min,
        price_max=price_max,
        limit=limit,
        offset=offset,
        session=session
    )

    return products


@router.get(
    '/products/{product_id}',
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