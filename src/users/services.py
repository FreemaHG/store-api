from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.auth.schemas.auth import UserCreateSchema
from src.auth.utils.password import get_password_hash
from src.users.models import User
from src.users.repositories import UserRepository


class UserServices:

    @classmethod
    async def update(cls, user_id: int, current_user: User, data: UserCreateSchema, session: AsyncSession) -> User | None:
        """
        Обновление данных пользователя
        :param user_id: id пользователя для обновления
        :param current_user: объект текущего пользователя
        :param data: новые данные пользователя
        :param session: объект асинхронной сессии
        :return: обновленный пользователь
        """

        if current_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_423_LOCKED,
                detail='Доступ запрещен'
            )

        data.password = await get_password_hash(password=data.password)
        updated_user = await UserRepository.update(user_id=user_id, data=data, session=session)

        return updated_user
