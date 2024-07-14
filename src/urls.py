from fastapi import FastAPI

from src.posts.routes.category import router as category_router
from src.posts.routes.product import router as product_router
from src.posts.routes.load_data.products import router as load_products_router
from src.auth.routes.auth import router as auth_router


def register_routers(app: FastAPI) -> FastAPI:
    """
    Регистрация роутов для API
    """
    app.include_router(category_router)
    app.include_router(product_router)
    app.include_router(load_products_router)
    app.include_router(auth_router)

    return app
