from sqladmin import ModelView
from starlette.requests import Request

from src.auth.utils.current_user import get_current_user
from src.database import async_session_maker
from src.users.models import User


class Userdmin(ModelView, model=User):

    name = "Пользователь"
    name_plural = "Пользователи"

    column_list = [User.id, User.username, User.email, User.registered_at, User.is_active, User.is_verified, User.is_superuser]
    column_searchable_list = [User.username]
    column_sortable_list = [User.id, User.username, User.email, User.registered_at, User.is_active, User.is_verified, User.is_superuser]

    column_labels = {
        User.username: "Логин",
        User.registered_at: "Дата регистрации",
        User.is_active: "Активен",
        User.is_verified: "Верификация",
        User.is_superuser: "Админ",
    }

    async def is_visible(self, request: Request) -> bool:
        """
        Видимость модели в админке
        """

        access_token = request.session.get('access_token')

        if not access_token:
            return False

        async with async_session_maker() as session:
            current_user = await get_current_user(token=access_token, session=session)

            # Видна только админу
            if not current_user or current_user.is_superuser is False:
                return False

            return True
