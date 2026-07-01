from typing import List, Optional
from sqlalchemy.exc import SQLAlchemyError

from models.user import User

class UserRepository:
    def __init__(self , session):
        self.session = session

    def get_by_username(self, username:str) -> User:
        return self.session.query(User).filter(User.username == username).first()

    def get_by_email(self, email:str) -> User:
        return self.session.query(User).filter(User.email == email).first()

    def get_by_id(self, id:str) ->Optional[User]:
        return self.session.query(User).filter(User.id == id).first()

    def get_all(self) -> List[User]:
        return self.session.query(User).all()

    def create(self, user) -> User:
        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def update(self, user:User) -> User:
        try:
            self.session.commit()
            self.session.refresh(user)
            return user
        except SQLAlchemyError:
            self.session.rollback()
            raise

    def delete(self, id:str) -> bool:
        try:
           user =  self.get_by_id(id)
           if user is None:
               return False
           self.session.delete(user)
           self.session.commit()
           return True
        except SQLAlchemyError:
            self.session.rollback()
            raise
