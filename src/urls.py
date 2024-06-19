from fastapi import FastAPI

from src.routes.category import router as category_router
from src.routes.product import router as product_router
from src.routes.load_data.products import router as load_products_router


def register_routers(app: FastAPI) -> FastAPI:
    """
    Регистрация роутов для API
    """
    app.include_router(category_router)
    app.include_router(product_router)
    app.include_router(load_products_router)

    return app