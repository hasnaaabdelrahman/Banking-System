import models.user as user
import datetime
import bcrypt

def hash_password(password:str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8') , bcrypt.gensalt(12))

def check_password(password:str, hashed_password:bytes) ->bool:
    return bcrypt.checkpw(password.encode('utf-8') , hashed_password)
