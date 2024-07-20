from sqladmin.authentication import AuthenticationBackend
from starlette import status
from starlette.requests import Request
from starlette.responses import RedirectResponse, Response

from src.auth.services import AuthService
from src.auth.utils.current_user import get_current_user
from src.database import async_session_maker


class AdminAuth(AuthenticationBackend):
    """
    Аутентификация, авторизация и выход из админки
    """

    async def login(self, request: Request) -> bool:
        """
        Авторизация по логину и паролю и обновление токена
        """
        form = await request.form()
        username, password = form["username"], form["password"]

        async with async_session_maker() as session:
            access_token = await AuthService.login(
                username=username,
                password=password,
                session=session
            )

        old_access_token = request.session.get('access_token')

        if not old_access_token:
            request.session["access_token"] = access_token
        else:
            request.session.update({"access_token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        """
        Выход из админки (завершение сеанса)
        """
        request.session.clear()
        return True

    # Вызывается для каждого запроса
    async def authenticate(self, request: Request) -> bool:
        """
        Проверка токена и прав администратора
        """
        access_token = request.session.get('access_token')

        if not access_token:
            return RedirectResponse('/admin/login')

        async with async_session_maker() as session:
            current_user = await get_current_user(token=access_token, session=session)

            if not current_user or current_user.is_superuser is False:
                return Response(status_code=status.HTTP_403_FORBIDDEN)

            return True
