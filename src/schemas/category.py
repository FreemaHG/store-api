from pydantic import BaseModel


class CategorySchema(BaseModel):
    """
    Вывод данных по меню
    """

    id: int
    name: str
    image: str


class ResponseSchema(BaseModel):
    """
    Cхема для возврата сообщения с ответом
    """

    message: str
