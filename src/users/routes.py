from typing import Annotated, Union

from fastapi import HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.auth.schemas.auth import UserCreateSchema
from src.database import get_async_session
from src.router import BaseRouter
from src.schemas import ResponseSchema
from src.users.models import User
from src.auth.utils.current_user import get_current_active_user
from src.users.schemas import UserOutSchema
from src.users.services import UserServices


router = BaseRouter(tags=['Пользователи'])

@router.get(
    "/users/me",
    name="Данные пользователя",
    description="Возврат данных пользователя",
    response_model=Union[UserOutSchema, ResponseSchema],
    responses={
        200: {'model': UserOutSchema},
        400: {'model': ResponseSchema},
        401: {'model': ResponseSchema},
    },
)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    """
    Возврат данных текущего пользователя
    """
    return current_user



@router.put(
    '/users/{user_id}',
    name="Обновление пользователя",
    description="Обновление данных пользователя",
    response_model=Union[UserOutSchema, ResponseSchema],
    responses={
        200: {'model': UserOutSchema},
        404: {'model': ResponseSchema},
    },
)
async def update_user(
    user_id: int,
    data: UserCreateSchema,
    current_user: Annotated[User, Depends(get_current_active_user)],
    session: AsyncSession = Depends(get_async_session)
):
    """
    Обновление данных пользователя
    """

    updated_user = await UserServices.update(
        user_id=user_id,
        current_user=current_user,
        data=data,
        session=session
    )

    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Пользователь не найден'
        )

    return updated_user
