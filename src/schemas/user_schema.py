from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    password: str
    role_id: int = 0
    email: str

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    username: str
    email: str
    password: str
    role_id: int


class UserSchemaEdit(BaseModel):
    username: str
    email: str
    password: str
    role_id: int
