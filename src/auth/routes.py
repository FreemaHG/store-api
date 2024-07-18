from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.auth.schemas import Token
from src.auth.services.register_user import authenticate_user
from src.auth.utils.token import create_access_token
from src.config import ACCESS_TOKEN_EXPIRE_MINUTES
from src.database import get_async_session
from src.router import BaseRouter


router = BaseRouter(tags=['Авторизация'])

@router.post(
    "/auth/token/",
    name="Авторизация",
    description="Авторизация пользователя и возврат токена",
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
