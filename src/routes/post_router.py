from fastapi import APIRouter, HTTPException
from src.routes.dependencies import UOWDep
from src.schemas.post_schema import PostSchemaAdd, PostSchemaEdit
from src.services.post_service import PostService

post_router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@post_router.get("")
async def get_posts(uow: UOWDep):
    try:
        posts = await PostService.get_posts(uow)
        return posts
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@post_router.get("/history")
async def get_post_history(uow: UOWDep):
    try:
        post_history = await PostService.get_post_history(uow)
        return post_history
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@post_router.post("")
async def add_post(uow: UOWDep, data: PostSchemaAdd):
    try:
        post_id = await PostService.add_post(uow, data)
        return {"Status": f"Success: post id{post_id} has been added"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@post_router.put("/{post_id}")
async def edit_post(uow: UOWDep, post_id: int, data: PostSchemaEdit):
    try:
        await PostService.edit_post(uow, post_id, data)
        return {"Status": f"Success: post id{post_id} has been edited"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})


@post_router.delete("")
async def delete_post(uow: UOWDep):
    try:
        await PostService.delete_one(uow)
        return {"Status": "Error: delete method is not implemented yet"}
    except Exception:
        raise HTTPException(status_code=500, detail={"Status": "Error"})
