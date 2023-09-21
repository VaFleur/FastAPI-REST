from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from src.mixin import MixinCRUD


class OperationBase(DeclarativeBase):
    pass


class Operation(OperationBase, MixinCRUD):
    __tablename__ = 'operation_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[str]
    figi: Mapped[str]
    instrument_type: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str]
