from typing import Text
from pydantic import BaseModel


class CommentSchema(BaseModel):
    id: int
    body: Text
    post_id: int

    class Config:
        from_attributes = True


class CommentSchemaAdd(BaseModel):
    body: Text
    post_id: int


class CommentSchemaEdit(BaseModel):
    body: Text


class CommentHistorySchema(BaseModel):
    id: int
    previous_body: Text
    new_body: Text
    post_id: int
    comment_id: int

    class Config:
        from_attributes = True


class CommentHistorySchemaAdd(BaseModel):
    previous_body: Text
    new_body: Text
    post_id: int
    comment_id: int
