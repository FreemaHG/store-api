from sqladmin import ModelView

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
        User.is_active: "Статус",
        User.is_verified: "Верификация",
        User.is_superuser: "Админ",
    }
