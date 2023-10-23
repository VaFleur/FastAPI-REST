from typing import Text
from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    header: str
    body: Text

    class Config:
        from_attributes = True


class PostSchemaAdd(BaseModel):
    header: str
    body: Text


class PostSchemaEdit(BaseModel):
    header: str
    body: Text


class PostHistorySchemaRead(BaseModel):
    id: int
    post_id: int
    previous_header: int
    previous_body: int
    new_header: int
    new_body: int

    class Config:
        from_attributes = True


class PostHistorySchemaAdd(BaseModel):
    post_id: int
    previous_header: int
    previous_body: int
    new_header: int
    new_body: int
