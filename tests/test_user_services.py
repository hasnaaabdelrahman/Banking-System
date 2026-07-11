import unittest
from assertpy import assert_that

from exceptions.user_exceptions import UserAlreadyExists, UserNotFound
from schemas.user_schema import UserLoginSchema, UserRegisterSchema
from services.user_services import UserService
from utils import password


class TestUserService(unittest.TestCase):
   def setUp(self):
       self.user = UserDouble(username='user_123',password='password@123',email='email@example.com',first_name='fuser',last_name='luser',age=20,img_url='https://example.com')
       self.user_repository = UserRepositorySpy()
       self.user_service = UserService(self.user_repository)

   def test_user_register(self):
        self.user_repository.user = None
        register_data = UserRegisterSchema(
            username='user_123',
            password='password@123',
            email='email@example.com',
            first_name='fuser',
            last_name='luser',
            age=20,
            img_url='https://example.com'
        )
        user =  self.user_service.register(register_data)
        assert_that(self.user.username).is_equal_to(user.username)

   def test_user_login(self):
       self.user_repository.user = self.user
       self.user.password = password.hash_password(self.user.password)
       login_data = UserLoginSchema(
           username="user_123",
           password="password@123"
       )
       user = self.user_service.login(login_data)
       assert_that(user.username).is_equal_to('user_123')

   def test_user_already_exists_will_raises_exception(self):
       self.user_repository.user = self.user
       with self.assertRaises(UserAlreadyExists):
           self.user_service.register(self.user_repository.user)

   def test_user_not_found_will_raises_exception(self):
       login_data = UserDouble(
           username = 'user123',
           password = 'password@123'
       )
       self.user_repository.user = None
       with self.assertRaises(UserNotFound):
           self.user_service.login(login_data)


class UserRepositorySpy:
    def __init__(self):
        self.user = None
        self.created_user = None
        self.logged_in_user = None

    def get_by_username(self, username):
        if self.user and self.user.username == username:
            return self.user
        return None

    def get_by_email(self, email):
        if self.user and self.user.email == email:
            return self.user
        return None

    def create(self, user):
        self.created_user = user
        return user


class UserDouble:
    def __init__(self, username = 'user_123',password='password@123',email = 'user@example.com',first_name = 'fuser',last_name = 'luser',age = 20,img_url ='https://example.com'):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.img_url = img_url

if __name__ == '__main__':
    unittest.main()