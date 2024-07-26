import random

from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models.product import Product
from src.products.repositories.product import ProductRepository


class ProductService:
    """
    Вывод товаров
    """

    # TODO Не используется!!!
    @classmethod
    async def get_list(
            cls,
            category_id: int,
            session: AsyncSession,
            title: str = None,
            price_min: float = None,
            price_max: float = None,
    ) -> list[Product] | None:
        """
        Возврат отфильтрованного списка товаров
        :param category_id: идентификатор категории
        :param title: название товара
        :param price_min: минимальная цена
        :param price_max: максимальная цена
        :param session: объект асинхронной сессии
        :return: список с товарами
        """

        filtered_products = await ProductRepository.get_list(
            category_id=category_id,
            title=title,
            price_min=price_min,
            price_max=price_max,
            session=session
        )
        # TODO Добавить кэширование

        return filtered_products

    @classmethod
    async def get(cls, product_id: int, session: AsyncSession) -> Product | None:
        """
        Возврат товара по id
        :param product_id: id товара
        :param session: объект асинхронной сессии
        :return: объект товара
        """
        post = await ProductRepository.get(product_id=product_id, session=session)
        # TODO Добавить кэширование

        return post
