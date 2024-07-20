from typing import Union

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas.auth import UserCreateSchema
from src.database import get_async_session
from src.router import BaseRouter
from src.schemas import ResponseSchema
from src.users.schemas import UserOutSchema
from src.auth.services import AuthService


router = BaseRouter(tags=['Регистрация и авторизация'])

@router.post(
    "/auth/register/",
    name="Регистрация",
    description="Регистрация и возврат данных пользователя",
    response_model=Union[UserOutSchema, ResponseSchema],
    responses={
        201: {'model': UserOutSchema},
        404: {'model': ResponseSchema},
    },
    status_code=201,
)
async def register_user(
        user_data: UserCreateSchema,
        session: AsyncSession = Depends(get_async_session)
):
    """
    Регистрация пользователя
    """
    user = await AuthService.register(user_data=user_data, session=session)

    return user
