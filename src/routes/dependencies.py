from src.repositories.post_repository import PostRepository
from src.repositories.comment_repository import CommentRepository
from src.services.post_service import PostService
from src.services.comment_service import CommentService


def comment_service():
    return CommentService(CommentRepository)


def post_service():
    return PostService(PostRepository)
