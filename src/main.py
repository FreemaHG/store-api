from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqladmin import Admin

from src.admin.models.category import CategoryAdmin
from src.admin.models.product import ProductAdmin
from src.admin.models.user import Userdmin
from src.auth.exceptions import UnauthorizedException, unauthorized_exception_handler, SignatureExpiredException, \
    signature_expired_exception_handler
from src.database import engine
from src.config import FRONTAGE_URL, DEBUG
from src.urls import register_routers


app = FastAPI(title='store', debug=DEBUG)
admin = Admin(app, engine)

# Регистрация роутеров
register_routers(app)

# Регистрация моделей в админке
admin.add_view(CategoryAdmin)
admin.add_view(ProductAdmin)
admin.add_view(Userdmin)

# URL, с которых разрешено делать запросы на сервер
origins = [FRONTAGE_URL]

# Добавляем в middleware Cors для связки фронта и бэка
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрация кастомных исключений
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)
app.add_exception_handler(SignatureExpiredException, signature_expired_exception_handler)
