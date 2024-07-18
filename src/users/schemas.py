from typing import Optional

from pydantic import EmailStr, BaseModel


class UsernameSchema(BaseModel):
    """
    Базовая схема с логином пользователя
    """
    username: str


class UserBaseSchema(UsernameSchema):
    """
    Схема с базовыми полями о пользователе
    """
    email: EmailStr
    avatar: Optional[str] = None


class UserOutSchema(UserBaseSchema):
    """
    Схема для вывода данных о пользователе
    """
    id: int
