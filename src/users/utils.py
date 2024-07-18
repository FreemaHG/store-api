from typing import Annotated

import jwt
from jwt import InvalidTokenError
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.config import oauth2_scheme
from src.auth.schemas.token import TokenData
from src.users.models import User
from src.users.repositories import UserRepository
from src.config import SECRET_KEY, ALGORITHM
from src.database import get_async_session


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        session: AsyncSession = Depends(get_async_session)
):
    """
    Возврат текущего пользователя
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверные учетные данные для проверки подлинности",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)

    except InvalidTokenError:
        raise credentials_exception

    user = await UserRepository.get(username=token_data.username, session=session)

    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    """
    Возврат текущего активного пользователя
    :param current_user: текущий пользователь
    """

    if current_user.is_active is False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь не активен")

    return current_user
