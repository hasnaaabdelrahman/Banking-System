from models.user import User
from schemas.user_schema import UserRegisterSchema, UserLoginSchema
from utils import password
from exceptions.user_exceptions import UserAlreadyExists , UserNotFound , EmailAlreadyExists , InvalidCredentials

class UserService:
    def __init__(self , user_repository):
        self.user_repository = user_repository

    def register(self,user_data : UserRegisterSchema) -> User:
        if self.user_repository.get_by_username(user_data.username):
            raise UserAlreadyExists('user already exists')
        if self.user_repository.get_by_email(user_data.email):
            raise EmailAlreadyExists('email already exists')

        user = User(
            username = user_data.username,
            email = user_data.email,
            password = user_data.password,
            first_name = user_data.first_name,
            last_name = user_data.last_name,
            age = user_data.age,
            img_url=user_data.img_url
        )

        user.password = password.hash_password(user.password)
        return self.user_repository.create(user)

    def login(self ,user_data: UserLoginSchema) -> User:
        user = self.user_repository.get_by_username(user_data.username)
        if not user:
            raise UserNotFound('user does not exist.')
        if not  password.check_password(user_data.password , user.password):
            raise InvalidCredentials('Invalid username or password.')
        return user