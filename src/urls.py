from fastapi import FastAPI

from src.routes.category import router as category_router


def register_routers(app: FastAPI) -> FastAPI:
    """
    Регистрация роутов для API
    """
    app.include_router(category_router)

    return app