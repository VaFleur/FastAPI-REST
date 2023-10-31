from fastapi import APIRouter
from src.routes.dependencies import UOWDep
from src.schemas.comment_schema import CommentSchemaAdd, CommentSchemaEdit
from src.services.comment_service import CommentService

comment_router = APIRouter(
    prefix="/comments",
    tags=["Comments"],
)


@comment_router.get("")
async def get_comments(uow: UOWDep):
    comments = await CommentService.get_comments(uow)
    return comments


@comment_router.get("/history")
async def get_comment_history(uow: UOWDep):
    comment_history = await CommentService.get_comment_history(uow)
    return comment_history


@comment_router.post("")
async def add_comment(uow: UOWDep, data: CommentSchemaAdd):
    comment_id = await CommentService.add_comment(uow, data)
    return {"Status": f"Comment id{comment_id} has been added"}


@comment_router.put("/{comment_id}")
async def edit_comment(uow: UOWDep, comment_id: int, data: CommentSchemaEdit):
    await CommentService.edit_comment(uow, comment_id, data)
    return {"Success": f"Comment id{comment_id} has been edited"}


@comment_router.delete("")
async def delete_comment(uow: UOWDep):
    await CommentService.delete_comment(uow)
    return {"Error": "Delete method is not implemented yet"}
