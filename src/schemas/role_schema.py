from pydantic import BaseModel


class RoleSchema(BaseModel):
    id: int
    name: str
    permissions: dict

    class Config:
        from_attributes = True


class RoleSchemaAdd(BaseModel):
    name: str
    permissions: dict


class RoleSchemaEdit(BaseModel):
    name: str
    permissions: dict
