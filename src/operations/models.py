from datetime import datetime
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class OperationBase(DeclarativeBase):
    pass


class Operation(OperationBase):
    __tablename__ = 'operation_table'

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[str] = mapped_column()
    figi: Mapped[str] = mapped_column()
    instrument_type: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(default=datetime.utcnow())
    type: Mapped[str] = mapped_column()
