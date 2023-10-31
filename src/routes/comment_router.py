from fastapi import APIRouter, HTTPException
from src.routes.dependencies import UOWDep
from src.schemas.comment_schema import CommentSchemaAdd, CommentSchemaEdit
from src.services.comment_service import CommentService

comment_router = APIRouter(
    prefix="/comments",
    tags=["Comments"],
)


@comment_router.get("")
async def get_comments(uow: UOWDep):
    try:
        comments = await CommentService.get_comments(uow)
        return comments
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@comment_router.get("/history")
async def get_comment_history(uow: UOWDep):
    try:
        comment_history = await CommentService.get_comment_history(uow)
        return comment_history
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@comment_router.post("")
async def add_comment(uow: UOWDep, data: CommentSchemaAdd):
    try:
        comment_id = await CommentService.add_comment(uow, data)
        return {"Status": f"Success: comment id{comment_id} has been added"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@comment_router.put("/{comment_id}")
async def edit_comment(uow: UOWDep, comment_id: int, data: CommentSchemaEdit):
    try:
        await CommentService.edit_comment(uow, comment_id, data)
        return {"Status": f"Success: comment id{comment_id} has been edited"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@comment_router.delete("")
async def delete_comment(uow: UOWDep):
    try:
        await CommentService.delete_comment(uow)
        return {"Status": "Error: delete method is not implemented yet"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})
