from pydantic import BaseModel


class ImageSchema(BaseModel):
    """
    Вывод url изображения к товару
    """
    url: str
