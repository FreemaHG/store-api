from passlib.context import CryptContext


# Контекст PassLib для хэширования и проверки паролей
# deprecated="auto" - использовать рекомендованные схемы хэширования и автоматически обновлять устаревшие
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Проверка паролей
    :param plain_password: пароль для сверки
    :param hashed_password: хэшированный пароль из БД
    """
    # Метод хэширует пароль для сверки и сверяет результат с хэшированным паролем из БД
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password: str) -> str:
    """
    Возврат хэша пароля
    :param password: пароль
    """
    return pwd_context.hash(password)
