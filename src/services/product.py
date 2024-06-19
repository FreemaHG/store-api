from sqlalchemy.ext.asyncio import AsyncSession

from src.models.product import Product
from src.repositories.product import ProductRepository


class ProductService:
    """
    Вывод товаров
    """

    @classmethod
    async def get_products(cls, session: AsyncSession) -> list[Product] | None:
        """
        Возврат списка товаров
        :param session: объект асинхронной сессии
        :return: список с товарами
        """
        products = await ProductRepository.get_list(session=session)

        return products
