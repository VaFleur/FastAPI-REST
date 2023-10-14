from pydantic import BaseModel


class RoleSchemaRead(BaseModel):
    id: int
    name: str
    permissions: dict

    class Config:
        from_attributes = True


class RoleSchemaAdd(BaseModel):
    name: str
    permissions: dict
