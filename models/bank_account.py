import uuid
class BankAccount:
    def __init__(self, user_id:str, account_number:str, account_type:str,  balance:float = 0.0, is_active:bool =True):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.balance = balance
        self.account_number = account_number
        self.account_type = account_type
        self.is_active = is_active
