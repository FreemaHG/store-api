from typing import Union, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.schemas.auth import UserCreateSchema
from src.router import BaseRouter
from src.users.models import User
from src.database import get_async_session
from src.schemas import ResponseSchema
from src.users.schemas import UserOutSchema
from src.users.services import RegisterUserServices
from src.users.utils import get_current_active_user


router = BaseRouter(tags=['Пользователи'])

@router.post(
    "/users/",
    name="Создание (регистрация) пользователя",
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
    user = await RegisterUserServices.register(user_data=user_data, session=session)

    return user


@router.get(
    "/users/me/",
    name="Данные пользователя",
    description="Возврат данных пользователя",
)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    """
    Возврат данных текущего пользователя
    """
    return current_user
