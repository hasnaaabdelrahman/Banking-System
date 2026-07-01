from models.user import User
from utils import password
from exceptions.user_exceptions import UserAlreadyExists , UserNotFound , EmailAlreadyExists , InvalidCredentials

class UserService:
    def __init__(self , user_repository):
        self.user_repository = user_repository

    def register(self,user : User) -> User:
        if self.user_repository.get_by_username(user.username):
            raise UserAlreadyExists('user already exists')
        if self.user_repository.get_by_email(user.email):
            raise EmailAlreadyExists('email already exists')
        user.password = password.hash_password(user.password)
        return self.user_repository.create(user)

    def login(self , username:str , user_password:str) -> User:
        user = self.user_repository.get_by_username(username)
        if not user:
            raise UserNotFound('user does not exist.')
        if not  password.check_password(user_password , user.password):
            raise InvalidCredentials('Invalid username or password.')
        return user