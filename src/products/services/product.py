import random

from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models.product import Product
from src.products.repositories.product import ProductRepository


class ProductService:
    """
    Вывод товаров
    """

    @classmethod
    async def get_list(cls, session: AsyncSession) -> list[Product] | None:
        """
        Возврат списка товаров
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        products = await ProductRepository.get_list(session=session)
        random.shuffle(products)  # Перемешиваем товары

        return products

    @classmethod
    async def get_filter_by_title(cls, title: str, session: AsyncSession) -> list[Product] | None:
        """
        Возврат списка товаров
        :param title: название товара
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        filtered_products = await ProductRepository.get_filter_by_title(title=title, session=session)

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

        return post
