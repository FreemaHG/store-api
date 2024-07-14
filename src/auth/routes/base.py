from fastapi import APIRouter


class BaseAPIRouter(APIRouter):
    """
    Базовый URL для авторизации
    """

    def __init__(self, *args, **kwargs):
        self.prefix = '/auth'
        super().__init__(*args, **kwargs, prefix=self.prefix)
