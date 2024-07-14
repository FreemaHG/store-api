from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User
from src.users.repositories import UserRepository
from src.auth.utils.password import get_password_hash
from src.users.schemas import UserCreateSchema


class RegisterUserServices:
    """
    Регистрация и авторизация нового пользователя
    """

    @classmethod
    async def register(cls, user_data: UserCreateSchema, session: AsyncSession) -> User:
        """
        Регистрация нового пользователя
        :param user_data: данные нового пользователя
        :param session: объект асинхронной сессии
        :return: объект нового пользователя
        """
        hash_password = get_password_hash(password=user_data.password)

        user = await UserRepository.create(
            new_user=user_data,
            hash_password=hash_password,
            session=session
        )

        return user
