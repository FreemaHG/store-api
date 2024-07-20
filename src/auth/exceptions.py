from starlette import status
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


class UnauthorizedException(HTTPException):
    """
    Класс для вывода исключений для неавторизованных пользователей
    """
    pass


async def unauthorized_exception_handler(request: Request, exc: HTTPException):
    """
    Кастомный обработчик ошибок для UnauthorizedException
    """
    return JSONResponse(
        {'detail': 'Неверные учетные данные для проверки подлинности'},
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Basic"}
    )


class SignatureExpiredException(HTTPException):
    """
    Класс для вывода исключений, если срок действия токена истек
    """
    pass


async def signature_expired_exception_handler(request: Request, exc: HTTPException):
    """
    Кастомный обработчик ошибок для UnauthorizedException
    """
    return JSONResponse(
        {'detail': 'Срок действия токена истек'},
        status_code=status.HTTP_401_UNAUTHORIZED,
        headers={"WWW-Authenticate": "Basic"}
    )