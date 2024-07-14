from typing import List

from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.posts.models.image import Image


class Product(Base):
    """
    Товары
    """
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))

    images: Mapped[List['Image']] = relationship('Image', backref='product', cascade='all, delete-orphan')
