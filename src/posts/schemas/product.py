from typing import List
from decimal import Decimal

from pydantic import BaseModel, field_validator

from src.posts.schemas.category import CategorySchema
from src.posts.schemas.image import ImageSchema


class ProductSchema(BaseModel):
    """
    Вывод данных по товару
    """

    id: int
    title: str
    description: str
    price: Decimal
    category: CategorySchema
    images: List[str]

    @field_validator('images', mode='before', check_fields=False)
    def serialize_images(cls, images: List[ImageSchema]) -> List[str]:
        """
        Возврат списка с URL изображений
        """
        return [image.url for image in images]
