from src.routes.comment_router import comment_router
from src.routes.post_router import post_router
from src.routes.role_router import role_router

all_routers = [
    comment_router,
    post_router,
    role_router,
]
