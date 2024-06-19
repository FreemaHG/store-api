from pydantic import BaseModel


class CategorySchema(BaseModel):
    """
    Вывод данных по меню
    """

    id: int
    name: str


class ResponseSchema(BaseModel):
    """
    Cхема для возврата сообщения с ответом
    """

    message: str
