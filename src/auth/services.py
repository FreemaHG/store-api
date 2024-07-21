from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.auth.schemas.auth import UserCreateSchema
from src.auth.utils.token import create_access_token
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES
from src.users.models import User
from src.users.repositories import UserRepository
from src.auth.utils.password import verify_password, get_password_hash


class AuthService:
    """
    Регистрация, аутентификация и авторизация пользователя
    """

    @classmethod
    async def register(cls, user_data: UserCreateSchema, session: AsyncSession) -> User:
        """
        Регистрация нового пользователя
        :param user_data: данные нового пользователя
        :param session: объект асинхронной сессии
        :return: объект нового пользователя
        """

        user = await UserRepository.get(username=user_data.username, session=session)

        if user:
            raise HTTPException(
                status_code=status.BAD_REQUEST,
                detail='Пользователь с таким логином уже зарегистрирован'
            )

        hash_password = await get_password_hash(password=user_data.password)

        new_user = await UserRepository.create(
            new_user=user_data,
            hash_password=hash_password,
            session=session
        )

        return new_user


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

    @classmethod
    async def login(cls, username: str, password: str, session: AsyncSession) -> str:
        """
        Авторизация пользователя (генерация и возврат токена аутентификации)
        :param username: логин
        :param password: пароль
        :param session: объект сессии
        :return: токен аутентификации
        """

        user = await cls.get_authenticate_user(username=username, password=password, session=session)

        if not user:
            from fastapi import HTTPException
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
