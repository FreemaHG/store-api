from fastapi.security import OAuth2PasswordBearer


# Указываем URL для получения токена клиентом (не создаем URL!!!)
# При использовании данной зависимости автоматически будет проверятся тип токена и сам токен в заголовках запросов
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token/")
