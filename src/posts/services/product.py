from sqlalchemy.ext.asyncio import AsyncSession

from src.posts.models.product import Product
from src.posts.repositories.product import ProductRepository


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

        return products

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
