from pydantic import BaseModel


class ResponseSchema(BaseModel):
    """
    Cхема для возврата сообщения с ответом
    """

    message: str
