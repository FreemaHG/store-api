from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Category(Base):
    """
    Категория товаров
    """
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
