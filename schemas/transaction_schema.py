import datetime

from  pydantic import BaseModel

from common.transaction_type import TransactionType


class TransactionSchema(BaseModel):
    account_id: str
    transaction_type: TransactionType
    amount: float
    date: datetime
