from datetime import datetime

from sqlalchemy import String, TIMESTAMP, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    """
    Пользователь
    """
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    avatar: Mapped[str] = mapped_column(String(300), nullable=True)
    registered_at: Mapped[str] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
