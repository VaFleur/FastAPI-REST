from abc import ABC, abstractmethod
from typing import Type
from src.models.comment_model import Comment
from src.models.post_model import Post
from src.models.role_model import Role
from src.database.database import async_session_maker
from src.models.user_model import User
from src.repositories.comment_repository import CommentRepository
from src.repositories.post_repository import PostRepository
from src.repositories.role_repository import RoleRepository
from src.repositories.user_repository import UserRepository


class IUnitOfWork(ABC):
    posts = Type[Post]
    comments = Type[Comment]
    roles = Type[Role]
    users = Type[User]

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, *args):
        pass

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.posts = PostRepository(self.session)
        self.comments = CommentRepository(self.session)
        self.roles = RoleRepository(self.session)
        self.users = UserRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
