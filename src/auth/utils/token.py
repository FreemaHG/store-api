from datetime import timedelta, datetime, timezone

import jwt

from src.config import SECRET_KEY, ALGORITHM


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Генерация токена аутентификации
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
