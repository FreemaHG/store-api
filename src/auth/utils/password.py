from passlib.context import CryptContext


# Контекст PassLib для хэширования и проверки паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password) -> bool:
    """
    Проверка паролей
    :param plain_password: пароль для сверки
    :param hashed_password: хэшированный пароль из БД
    """
    # Метод хэширует пароль для сверки и сверяет результат с хэшированным паролем из БД
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    """
    Получить хэш пароля
    """
    return pwd_context.hash(password)
