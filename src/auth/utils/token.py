from datetime import timedelta, datetime, timezone
from fastapi import Request, HTTPException, status

import jwt

from src.config import SECRET_KEY, ALGORITHM


async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Генерация JSON Web Token (JWT) для аутентификации пользователей
    """
    to_encode = data.copy()

    if expires_delta:
        # Прибавляем к текущей дате время жизни токена
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # По умолчанию время жизни токена 30 дней
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    # Записываем в токен время истечения срока токена по ключу "exp"
    to_encode.update({"exp": expire})

    # Кодируем данные в токене
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def get_token(request: Request) -> str:
    """
    Проверка и возврат access-токена из кук запроса
    :param request: объект запроса
    :return: токен
    """
    access_token = request.cookies.get('users_access_token')

    if not access_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Токен не найден')

    return access_token
