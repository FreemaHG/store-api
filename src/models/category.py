from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.models.product import Product


class Category(Base):
    """
    Категория товаров
    """
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    image: Mapped[str] = mapped_column(String(300), nullable=True)

    products: Mapped[List['Product']] = relationship('Product', backref='category', cascade='all, delete-orphan')
