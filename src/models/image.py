from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Image(Base):
    """
    Изображения к товарам
    """
    __tablename__ = 'image'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    url: Mapped[str] = mapped_column(String(300))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
