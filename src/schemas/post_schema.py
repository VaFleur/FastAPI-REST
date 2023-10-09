from typing import Text
from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    header: str
    body: Text

    class Config:
        from_attributes = True


class PostAdd(BaseModel):
    header: str
    body: Text
