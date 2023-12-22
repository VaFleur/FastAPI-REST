from src.schemas.role_schema import RoleSchemaAdd, RoleSchemaEdit
from src.utils.unit_of_work import IUnitOfWork


class RoleService:
    @staticmethod
    async def get_roles(uow: IUnitOfWork):
        async with uow:
            roles = await uow.roles.find_all()
            return roles

    @staticmethod
    async def add_role(uow: IUnitOfWork, data: RoleSchemaAdd):
        data_dict = data.model_dump()
        async with uow:
            role_id = await uow.roles.add_one(data_dict)
            await uow.commit()
            return role_id

    @staticmethod
    async def edit_role(uow: IUnitOfWork, role_id: int, data: RoleSchemaEdit):
        data_dict = data.model_dump()
        async with uow:
            role_id = await uow.roles.edit_one(role_id, data_dict)
            await uow.commit()
            return role_id

    @staticmethod
    async def delete_role(uow: IUnitOfWork):
        async with uow:
            await uow.roles.delete_one()
