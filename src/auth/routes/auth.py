from datetime import timedelta
from typing import Annotated, Union

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.auth.models import User
from src.auth.routes.base import BaseAPIRouter
from src.auth.schemas.token import Token
from src.auth.schemas.user import UserOutSchema, UserCreateSchema
from src.auth.services.register_user import authenticate_user, RegisterUserServices
from src.auth.utils.token import create_access_token
from src.auth.utils.user import get_current_active_user
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES
from src.database import get_async_session
from src.schemas.response import ResponseSchema


router = BaseAPIRouter(tags=['auth'])

@router.post(
    "/register/",
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
    user = await RegisterUserServices.register(user_data=user_data, session=session)

    return user


@router.post(
    "/token/",
    name="Аутентификация",
    description="Аутентификация пользователя и возврат токена",
    response_model=Token,
    responses={
        201: {'model': Token}
    },
)
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: AsyncSession = Depends(get_async_session)
):
    """
    Авторизация пользователя и возврат токена
    """
    user = await authenticate_user(username=form_data.username, password=form_data.password, session=session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не найден",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    # Возврат bearer-токена (для сторонних API)
    return Token(access_token=access_token, token_type="bearer")


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
