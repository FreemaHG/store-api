from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.models.product import Product


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
        query = select(Product)\
            .options(joinedload(Product.images))\
            .options(joinedload(Product.category))\
            .where(Product.id == product_id)

        product = await session.execute(query)

        return product.unique().scalar_one_or_none()

    @classmethod
    async def get_list(cls, session: AsyncSession) -> List[Product]:
        """
        Возврат всех товаров
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        query = select(Product).options(joinedload(Product.images)).options(joinedload(Product.category))
        res = await session.execute(query)
        products = res.scalars().unique()

        return list(products)

    @classmethod
    async def get_filter_list(cls, category_id: int, session: AsyncSession) -> List[Product]:
        """
        Возврат товаров определенной категории
        :param category_id: идентификатор категории
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        query = select(Product).where(Product.category_id == category_id)
        res = await session.execute(query)
        products = res.scalars().all()

        return list(products)
