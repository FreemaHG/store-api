from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.schemas.user import UserCreateSchema


class UserRepository:
    """
    CRUD-операции с категориями
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