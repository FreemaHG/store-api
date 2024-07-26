from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.products.models.product import Product


class ProductRepository:
    """
    CRUD-операции с товарами
    """

    @classmethod
    async def get(cls, product_id: int, session: AsyncSession) -> Product | None:
        """
        Возврат товара по id
        :param product_id: идентификатор товара
        :param session: объект асинхронной сессии
        :return: объект товара | None
        """
        query = select(Product).options(joinedload(Product.images)).options(joinedload(Product.category))\
            .where(Product.id == product_id)

        product = await session.execute(query)

        return product.unique().scalar_one_or_none()

    @classmethod
    async def get_list(
            cls,
            category_id: int,
            session: AsyncSession,
            title: str = None,
            price_min: float = None,
            price_max: float = None,
            limit: int = None,
            offset: int = None,
    ) -> List[Product]:
        """
        Фильтрация и возврат товаров
        :param category_id: идентификатор категории
        :param title: название товара
        :param price_min: минимальная цена
        :param price_max: максимальная цена
        :param limit: кол-во возвращаемых записей
        :param offset: сдвиг в наборе результатов
        :param session: объект асинхронной сессии
        :return: список с отфильтрованными товарами
        """
        query = select(Product).options(joinedload(Product.images)).options(joinedload(Product.category)).order_by(Product.id)

        if category_id:
            query = query.where(Product.category_id == category_id)

        if title:
            query = query.where(Product.title.ilike(f'%{title}%'))

        if price_min:
            query = query.where(Product.price >= price_min)

        if price_max:
            query = query.where(Product.price <= price_max)

        if limit is not None and offset is not None:
            query = query.limit(limit).offset(offset)

        res = await session.execute(query)
        products = res.scalars().unique()

        return list(products)
