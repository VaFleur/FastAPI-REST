from typing import Text
from pydantic import BaseModel


class CommentSchema(BaseModel):
    id: int
    body: Text
    post_id: int

    class Config:
        from_attributes = True


class CommentAdd(BaseModel):
    body: Text
    post_id: int
