from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.posts.models.category import Category
from src.posts.schemas.category import CategorySchema


class CategoryCRUDRepository:
    """
    CRUD-операции с категориями
    """

    @classmethod
    async def create(cls, name: str, session: AsyncSession) -> Category:
        """
        Создание категории
        :param name: название категории
        :param session: объект асинхронной сессии
        :return: объект нового блюда
        """
        category = Category(mame=name)
        session.add(category)
        await session.commit()

        return category

    @classmethod
    async def get(cls, category_id: int, session: AsyncSession) -> Category | None:
        """
        Возврат категории по id
        :param category_id: идентификатор категории
        :param session: объект асинхронной сессии
        :return: объект категории | None
        """
        query = select(Category).where(Category.id == category_id)
        category = await session.execute(query)

        return category.scalar_one_or_none()

    @classmethod
    async def update(cls, category_id: int, name: CategorySchema, session: AsyncSession) -> Category | None:
        """
        Обновление категории по id
        :param category_id: идентификатор категории
        :param name: новое название категории
        :param session: объект асинхронной сессии
        :return: обновленный объект категории | None
        """
        # model_dump(exclude_unset=True) - распаковывает явно переданные поля в patch-запросе
        query = (
            update(Category)
            .where(Category.id == category_id)
            .values(name.model_dump(exclude_unset=True))
        )
        await session.execute(query)
        await session.commit()

        return session.query(Category).get(id=category_id)

    @classmethod
    async def delete(cls, category_id: int, session: AsyncSession) -> None:
        """
        Удаление категории по id
        :param category_id: идентификатор категории
        :param session: объект асинхронной сессии
        :return: None
        """
        query = delete(Category).where(Category.id == category_id)
        await session.execute(query)
        await session.commit()


class CategoryListRepository:
    """
    Возврат списка категорий товаров
    """

    @classmethod
    async def get_list(cls, session: AsyncSession) -> List[Category]:
        """
        Возврат всех категорий товаров
        :param session: объект асинхронной сессии
        :return: список с категориями
        """
        query = select(Category)
        res = await session.execute(query)
        categories = res.scalars().all()

        return list(categories)
