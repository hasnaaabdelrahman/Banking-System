import datetime
import uuid

class Transaction:
    def __init__(self, transaction_type:str, account_id:str, date:datetime.date, amount:float=0.0):
        self.id = str(uuid.uuid4())
        self.transaction_type = transaction_type
        self.amount = amount
        self.account_id = account_id
        self.date = date