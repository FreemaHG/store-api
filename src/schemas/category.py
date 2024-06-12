from pydantic import BaseModel


class CategorySchema(BaseModel):
    """
    Вывод данных по меню
    """

    id: int
    name: str
