from fastapi import APIRouter


class BaseRouter(APIRouter):
    """
    Базовый URL и версия API
    """

    def __init__(self, *args, **kwargs):
        self.prefix = '/api/v1'
        super().__init__(*args, **kwargs, prefix=self.prefix)
