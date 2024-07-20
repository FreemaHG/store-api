from datetime import timedelta

from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.exceptions import HTTPException

from src.auth.services.auth import AuthService
from src.auth.utils.token import create_access_token
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES


class AccessTokenService:
    """
    Аутентификация пользователя, генерация и возврат токена
    """

    @classmethod
    async def generate(cls, username: str, password: str, session: AsyncSession) -> str:
        """
        Генерация и возврат токена аутентификации
        :param username: логин
        :param password: пароль
        :param session: объект сессии
        :return: сгенерированный токен
        """

        user = await AuthService.get_authenticate_user(username=username, password=password, session=session)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный логин или пароль",
            )

        # Время жизни токена
        access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        # Генерируем токен аутентификации (записываем в токен username)
        access_token = await create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )

        return access_token
