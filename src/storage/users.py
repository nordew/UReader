from typing import Optional, List
from sqlalchemy.orm import Session
from UReader.src.models.users import Users
from UReader.src.schemas.users import UserCreate, UserUpdate
from abc import abstractmethod

class UserInterface:

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[Users]:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[Users]:
        raise NotImplementedError

    @abstractmethod
    def get_users(self, skip: int = 0, limit: int = 10) -> List[Users]:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, user: UserCreate) -> Users:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user_id: int, user: UserUpdate) -> Users:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id: int) -> Users:
        raise NotImplementedError

class UserStorage(UserInterface):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_user_by_id(self, user_id: int) -> Optional[Users]:
        return self.db_session.query(Users).filter(Users.id == user_id).first()

    def get_user_by_email(self, email: str) -> Optional[Users]:
        return self.db_session.query(Users).filter(Users.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 10) -> List[Users]:
        return self.db_session.query(Users).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate) -> Users:
        db_user = Users(
            email=user.email,
            hashed_password=user.hashed_password,  # assuming you store hashed passwords
            full_name=user.full_name
        )
        self.db_session.add(db_user)
        self.db_session.commit()
        self.db_session.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user: UserUpdate) -> Users:
        db_user = self.get_user_by_id(user_id)
        if db_user:
            for key, value in user.dict(exclude_unset=True).items():
                setattr(db_user, key, value)
            self.db_session.commit()
            self.db_session.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> Users:
        db_user = self.get_user_by_id(user_id)
        if db_user:
            self.db_session.delete(db_user)
            self.db_session.commit()
        return db_user
