import random

import requests
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.posts.models.image import Image
from src.posts.models.product import Product
from src.posts.routes.base import BaseAPIRouter
from src.posts.schemas.category import ResponseSchema


router = BaseAPIRouter(tags=['Загрузка данных'])

@router.get(
    '/load_data',
    responses={
        200: {'model': ResponseSchema}
    },
)
async def load_data(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Загрузка товаров
    """
    response = requests.get('https://api.escuelajs.co/api/v1/products')
    products = response.json()
    new_products = []

    for prod in products:
        product = Product(
            title=prod['title'],
            description=prod['description'],
            price=prod['price'],
            category_id=random.randint(1, 5),
            images=[Image(url=img) for img in prod['images']]
        )

        new_products.append(product)

    session.add_all(new_products)
    await session.commit()

    return {"message": f"Успешно загружено {len(new_products)} товаров"}
