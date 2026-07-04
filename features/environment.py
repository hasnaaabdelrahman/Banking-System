from services.user.user_services import UserService
from repositories.user_repository import UserRepository
from models.user import User
from DB.db import session

def before_scenario(context, scenario):
    db = session()

    db.query(User).delete()
    db.commit()

    context.user_service = UserService(UserRepository(db))