from typing import Optional

from pydantic import EmailStr, BaseModel


class UserBaseSchema(BaseModel):
    """
    Схема с базовыми полями о пользователе
    """
    username: str
    email: EmailStr
    avatar: Optional[str] = None


class UserOutSchema(UserBaseSchema):
    """
    Схема для вывода данных о пользователе
    """
    id: int

class UserCreateSchema(UserBaseSchema):
    """
    Схема для регистрации пользователя
    """
    password: str
