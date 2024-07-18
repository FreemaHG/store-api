from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqladmin import Admin

from src.admin.category import CategoryAdmin
from src.admin.product import ProductAdmin
from src.admin.user import Userdmin
from src.database import engine
from src.config import FRONTAGE_URL, DEBUG
from src.urls import register_routers
from src.exceptions import CustomApiException, custom_api_exception_handler


app = FastAPI(title='store', debug=DEBUG)
admin = Admin(app, engine)

# Регистрация роутеров
register_routers(app)

# Регистрация моделей в админке
admin.add_view(CategoryAdmin)
admin.add_view(ProductAdmin)
admin.add_view(Userdmin)

# Регистрация кастомного исключения
app.add_exception_handler(CustomApiException, custom_api_exception_handler)

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
