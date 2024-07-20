from typing import Annotated

from fastapi import Depends

from src.router import BaseRouter
from src.users.models import User
from src.auth.utils.current_user import get_current_active_user


router = BaseRouter(tags=['Пользователи'])

@router.get(
    "/users/me/",
    name="Данные пользователя",
    description="Возврат данных пользователя",
)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    """
    Возврат данных текущего пользователя
    """
    return current_user
