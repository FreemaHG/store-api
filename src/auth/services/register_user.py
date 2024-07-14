from sqlalchemy.ext.asyncio import AsyncSession

from src.users.models import User
from src.users.repositories import UserRepository
from src.auth.utils.password import verify_password


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
