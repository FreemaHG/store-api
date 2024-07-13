from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqladmin import Admin

from src.admin import CategoryAdmin, ProductAdmin
from src.database import engine
from src.config import FRONTAGE_URL
from src.urls import register_routers
from src.utils.exceptions import CustomApiException, custom_api_exception_handler


app = FastAPI(title='store', debug=True)
admin = Admin(app, engine)

# Регистрация роутеров
register_routers(app)

# Регистрация моделей в админке
admin.add_view(CategoryAdmin)
admin.add_view(ProductAdmin)

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
