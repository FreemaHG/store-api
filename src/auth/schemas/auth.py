from pydantic import BaseModel

from src.users.schemas import UsernameSchema, UserBaseSchema


class PasswordSchema(BaseModel):
    """
    Базовая схема с паролем
    """
    password: str


class UserCreateSchema(UserBaseSchema, PasswordSchema):
    """
    Схема для регистрации пользователя
    """
    pass


class LoginSchema(UsernameSchema, PasswordSchema):
    """
    Схема для авторизации
    """
    pass
