from fastapi import APIRouter, HTTPException
from src.routes.dependencies import UOWDep
from src.schemas.role_schema import RoleSchemaAdd, RoleSchemaEdit
from src.services.role_service import RoleService

role_router = APIRouter(
    prefix="/roles",
    tags=["Roles"],
)


@role_router.get("")
async def get_roles(uow: UOWDep):
    try:
        roles = await RoleService.get_roles(uow)
        return roles
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@role_router.post("")
async def add_role(uow: UOWDep, data: RoleSchemaAdd):
    try:
        role_id = await RoleService.add_role(uow, data)
        return {"Status": f"Success: role id{role_id} has been added"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@role_router.put("/{role_id}")
async def edit_role(uow: UOWDep, role_id: int, data: RoleSchemaEdit):
    try:
        await RoleService.edit_role(uow, role_id, data)
        return {"Status": f"Success: role id{role_id} has been edited"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@role_router.delete("")
async def delete_role(uow: UOWDep):
    try:
        await RoleService.delete_role(uow)
        return {"Status": "Error: delete method is not implemented yet"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})
