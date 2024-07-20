import requests
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.products.models.category import Category
from src.products.models.image import Image
from src.products.models.product import Product
from src.products.schemas.category import ResponseSchema
from src.router import BaseRouter


router = BaseRouter(tags=['Загрузка данных'])

@router.get(
    '/load_data/',
    name="Загрузка товаров",
    description="Загрузка данных по товарам из стороннего API",
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
    products = requests.get('https://api.escuelajs.co/api/v1/products').json()
    new_categories = []
    new_products = []
    added_categories = []

    for product in products:
        category = product['category']

        if category['name'] not in added_categories:
            new_category = Category(
                name=category['name'],
                image=category['image'],
            )
            new_categories.append(new_category)
            added_categories.append(category['name'])

        else:
            new_category = [new_category for new_category in new_categories if new_category.name == category['name']][0]

        new_product = Product(
            title=product['title'],
            description=product['description'],
            price=product['price'],
            category=new_category,
            images=[Image(url=img) for img in product['images']]
        )

        new_products.append(new_product)

    session.add_all(new_products)
    await session.commit()

    return {"message": f"Успешно загружено {len(new_products)} товаров"}
