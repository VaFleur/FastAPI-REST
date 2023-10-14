from typing import Annotated
from fastapi import APIRouter, Depends
from src.routes.dependencies import comment_service
from src.schemas.comment_schema import CommentSchemaAdd
from src.services.comment_service import CommentService

comment_router = APIRouter(
    prefix="/comments",
    tags=["Comments"],
)


@comment_router.post("")
async def add_comment(schema: CommentSchemaAdd,
                      comments_service: Annotated[CommentService, Depends(comment_service)],
                      ):
    comment_id = await comments_service.add_comment(schema)
    return {"comment_id": comment_id}


@comment_router.get("")
async def get_comments(
        comments_service: Annotated[CommentService, Depends(comment_service)],
):
    comments = await comments_service.get_comments()
    return comments
