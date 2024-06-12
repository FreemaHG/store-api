from fastapi import APIRouter


class BaseAPIRouter(APIRouter):
    """
    Базовый URL и с версией API
    """

    def __init__(self, *args, **kwargs):
        self.prefix = '/api/v1'
        super().__init__(*args, **kwargs, prefix=self.prefix)
