from pydantic import BaseModel


class Resp(BaseModel):
    code: int = ...
    msg: str = ""
    data: dict = {}
