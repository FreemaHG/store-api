from pydantic import BaseModel


class Token(BaseModel):
    """
    Схема для возврата данных о токене
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Схема для проверки данных для получения токена
    """
    username: str | None = None
