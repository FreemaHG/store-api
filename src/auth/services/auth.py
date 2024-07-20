from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User
from src.users.repositories import UserRepository
from src.auth.utils.password import verify_password


class AuthService:
    """
    Регистрация, аутентификация, авторизация и возврат пользователя
    """

    @classmethod
    async def get_authenticate_user(cls, username: str, password: str, session: AsyncSession) -> User | None:
        """
        Возврат аутентифицированного пользователя
        :param username: логин пользователя
        :param password: пароль пользователя
        :param session: объект асинхронной сессии
        :return: объект пользователя
        """
        user = await UserRepository.get(username=username, session=session)

        if not user or await verify_password(plain_password=password, hashed_password=user.password) is False:
            return None

        return user
