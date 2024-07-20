from typing import Annotated

import jwt
from jwt import InvalidTokenError, ExpiredSignatureError
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.exceptions import UnauthorizedException, SignatureExpiredException
from src.auth.schemas.token import TokenData
from src.auth.utils.token import get_token
from src.users.models import User
from src.users.repositories import UserRepository
from src.config import SECRET_KEY, ALGORITHM
from src.database import get_async_session


async def get_current_user(
        token: str = Depends(get_token),
        session: AsyncSession = Depends(get_async_session)
):
    """
    Возврат текущего пользователя
    """

    try:
        # Декодируем данные из токена
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    except ExpiredSignatureError:
        # Если срок действия токена истек
        # дата истечения срока действия токена автоматически декодируется из токена по ключу "exp" и сравнивается с текущим временем
        raise SignatureExpiredException(status_code=status.HTTP_401_UNAUTHORIZED)

    except InvalidTokenError:
        raise UnauthorizedException(status_code=status.HTTP_401_UNAUTHORIZED)

    # Извлекаем username из токена
    username: str = payload.get("sub")

    if username is None:
        # raise credentials_exception
        raise UnauthorizedException

    token_data = TokenData(username=username)

    user = await UserRepository.get(username=token_data.username, session=session)

    if user is None:
        raise UnauthorizedException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    """
    Возврат текущего активного пользователя
    :param current_user: текущий пользователь
    """

    if current_user.is_active is False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пользователь не активен")

    return current_user
