from typing import Annotated
from fastapi import APIRouter, Depends
from src.routes.dependencies import UOWDep
from src.schemas.comment_schema import CommentSchemaAdd
from src.services.comment_service import CommentService

comment_router = APIRouter(
    prefix="/comments",
    tags=["Comments"],
)


@comment_router.get("")
async def get_comments(uow: UOWDep):
    pass


@comment_router.post("")
async def add_comment(uow: UOWDep):
    pass
