from services.user.user_services import UserService
from repositories.user_repository import UserRepository
from DB.db import session

def before_all(context):
    print(">>> before_all is running")
    db = session()
    user_repository = UserRepository(db)
    context.user_service = UserService(user_repository)

