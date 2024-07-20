from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response

from src.auth.schemas.auth import LoginSchema
from src.auth.schemas.token import Token
from src.auth.services import AuthService
from src.database import get_async_session
from src.router import BaseRouter


router = BaseRouter(tags=['Регистрация и авторизация'])

@router.post(
    "/auth/login/",
    name="Авторизация",
    description="Авторизация пользователя и возврат токена",
    response_model=Token,
    responses={
        201: {'model': Token}
    },
)
async def login(
        response: Response,
        login_data: LoginSchema,
        session: AsyncSession = Depends(get_async_session)
) -> Token:
    """
    Авторизация пользователя
    """

    access_token = await AuthService.login(
        username=login_data.username,
        password=login_data.password,
        session=session
    )
    response.set_cookie(key="access_token", value=access_token, httponly=True)

    return Token(access_token=access_token, token_type="bearer")


@router.post(
    "/auth/logout/",
    name="Выход",
    description="Выход пользователя из системы",
)
async def logout(response: Response):
    """
    Выход из системы
    """
    response.delete_cookie(key="access_token")

    return {'message': 'Пользователь успешно вышел из системы'}
