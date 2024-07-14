from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.auth.repositories import UserRepository
from src.auth.schemas.user import UserCreateSchema
from src.auth.utils.password import verify_password, get_password_hash


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




async def authenticate_user(username: str, password: str, session: AsyncSession) -> User | bool:
    """
    Возврат аутентифицированного пользователя
    :param username: логин пользователя
    :param password: пароль пользователя
    :param session: объект асинхронной сессии
    :return: объект пользователя
    """
    user = await UserRepository.get(username=username, session=session)

    if not user:
        return False

    if not verify_password(password, user.password):
        return False

    return user
