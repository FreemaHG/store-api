from sqlalchemy.ext.asyncio import AsyncSession

from src.products.models.category import Category
from src.products.repositories.caterory import CategoryListRepository


class CategoryService:
    """
    Вывод категорий
    """

    @classmethod
    async def get_categories(cls, session: AsyncSession) -> list[Category] | None:
        """
        Возврат списка категорий товаров
        :param session: объект асинхронной сессии
        :return: список с категориями
        """
        categories = await CategoryListRepository.get_list(session=session)
        # TODO Добавить кэширование

        return categories
