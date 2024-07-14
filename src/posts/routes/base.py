from fastapi import APIRouter


class BaseAPIRouter(APIRouter):
    """
    Базовый URL для магазинного функционала
    """

    def __init__(self, *args, **kwargs):
        self.prefix = '/store'
        super().__init__(*args, **kwargs, prefix=self.prefix)
