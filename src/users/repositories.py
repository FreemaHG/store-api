from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas.auth import UserCreateSchema
from src.users.models import User


class UserRepository:
    """
    Создание и возврат пользователя
    """

    @classmethod
    async def create(cls, new_user: UserCreateSchema, hash_password:str, session: AsyncSession) -> User:
        """
        Создание нового пользователя
        :param new_user: данные нового пользователя
        :param hash_password: хэшированный пароль
        :param session: объект асинхронной сессии
        :return: объект нового пользователя
        """

        query = insert(User).values(
            username=new_user.username,
            email=new_user.email,
            avatar=new_user.avatar,
            password=hash_password,
        ).returning(User)

        result = await session.execute(query)
        await session.commit()

        return result.scalar()

    @classmethod
    async def get(cls, username: str, session: AsyncSession) -> User | None:
        """
        Возврат пользователя по username
        :param username: имя пользователя
        :param session: объект асинхронной сессии
        :return: объект пользователя | None
        """
        query = select(User).where(User.username == username)
        user = await session.execute(query)

        return user.scalar_one_or_none()

    @classmethod
    async def update(cls, user_id: int, data: UserCreateSchema, session: AsyncSession) -> User | None:
        """
        Обновление данных пользователя
        :param user_id: id пользователя
        :param data: новые данные
        :param session: объект асинхронной сессии
        :return: обновленный объект пользователя
        """

        query = update(User).where(User.id == user_id).values(data.model_dump(exclude_unset=True)).returning(User)
        result = await session.execute(query)
        await session.commit()

        updated_user = result.scalar()

        return updated_user
