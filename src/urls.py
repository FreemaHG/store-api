from fastapi import FastAPI

from src.products.routes.category import router as category_router
from src.products.routes.product import router as product_router
from src.products.routes.load_data.products import router as load_products_router
from src.auth.routes.login import router as login_router
from src.auth.routes.register import router as register_router
from src.users.routes import router as user_router


def register_routers(app: FastAPI) -> FastAPI:
    """
    Регистрация роутов для API
    """
    app.include_router(category_router)
    app.include_router(product_router)
    app.include_router(load_products_router)
    app.include_router(user_router)
    app.include_router(login_router)
    app.include_router(register_router)

    return app
