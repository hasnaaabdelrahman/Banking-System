import datetime
import uuid
from sqlalchemy import Float, String, ForeignKey, DateTime , Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from DB.db import Base
from common.transaction_type import TransactionType

class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    account_id: Mapped[str] = mapped_column(
        ForeignKey("bank_account.id"),
        nullable=False
    )
    transaction_type: Mapped[TransactionType] = mapped_column(
        Enum(TransactionType),
        nullable=False,
    )
    amount: Mapped[float] = mapped_column(
        Float,
        default=0.0,
    )
    date: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now,
    )
    bank_account= relationship(
        "BankAccount",
        back_populates="transactions",
    )
