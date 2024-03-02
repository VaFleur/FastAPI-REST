from pydantic import BaseModel


class UserRead(BaseModel):
    id: int
    username: str
    hashed_password: str
    role_id: int = 0
    email: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    email: str
    hashed_password: str
    role_id: int


class UserUpdate(BaseModel):
    username: str
    email: str
    hashed_password: str
    role_id: int


class UserDelete(BaseModel):
    id: int
