from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.auth.schemas.auth import UserCreateSchema
from src.users.models import User
from src.users.repositories import UserRepository
from src.auth.utils.password import get_password_hash


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

        try:
            user = await UserRepository.create(
                new_user=user_data,
                hash_password=hash_password,
                session=session
            )
        except IntegrityError:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Пользователь с таким username уже зарегистрирован'
            )

        return user
