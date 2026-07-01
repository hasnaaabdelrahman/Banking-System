import unittest

from models import user
from services.user.user_services import UserService
from utils import password


class TestUserService(unittest.TestCase):
   def setUp(self):
       self.user = UserDouble(username='user_123',
                              password='password@123',
                              email='email@example.com',
                              first_name='fuser',
                              last_name='luser',
                              age=20,
                              image='https://example.com')

       self.user_repository = UserRepositorySpy()
       self.user_service = UserService(self.user_repository)

   def test_user_register(self):
        self.user_repository.user = None
        user =  self.user_service.register(self.user)
        self.assertEqual(self.user , user)
        self.assertEqual(self.user_repository.created_user , self.user)

   def test_user_login(self):
       self.user.password = password.hash_password(self.user.password)
       self.user_repository.user = self.user
       user = self.user_service.login("user_123", "password@123")
       self.assertEqual(self.user, user)

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
    def __init__(self, username = 'user_123',
                 password='password@123',
                 email = 'user@example.com',
                 first_name = 'fuser',
                 last_name = 'luser',
                 age = 20,
                 image ='https://example.com'):
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.image = image

if __name__ == '__main__':
    unittest.main()